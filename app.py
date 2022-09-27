# main python file
import os
import random
import MySQLdb
from flask import Flask, render_template, url_for, redirect, request, session
from flask_mysqldb import MySQL
import yaml
from flask_selfdoc import Autodoc

app = Flask(__name__)
auto = Autodoc(app)
app.secret_key = os.urandom(16)

db = yaml.safe_load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)


def mysql_create_connection():
    cursor = mysql.connection.cursor()
    return cursor


@app.route('/home', methods=['GET', 'POST'])
@auto.doc()
def home():
    """
    If Place Owner, display the QR Code
        Form Data:
            place_id: identification number of a place
            place_name: name registered in the database
            qr_size: size property for resizing the QR displayed

    Else If Agent, display the list of Visitors Registered
        Form Data:
            Agent_id: identification number of the Agent logged in

    Else If Hospital, display list of editable vistors (wait for next  sprint)
        Form Data:
            Hospital_id: identification number of the Hospital logged in

    Else, display scanner page(wait for next sprint)
        Form Data:        
            name: name of the Visitor registered
    """
    headings = ("Visitor Name", "Address", "Email",
                "Phone Number", "Infection Status")
    if 'place_id' in session:
        qr_place_id = session['place_id']
        place_name = session['place_name']
        if request.method == 'POST' and 'qr_size' in request.form:
            qr_size = request.form.get('qr_size')
            return render_template('Home.html', loggedIn=True, qr_id=qr_place_id, qrSize=qr_size, place_name=place_name)
        else:
            return render_template('Home.html', loggedIn=True, qr_id=qr_place_id, qrSize=250, place_name=place_name)
    elif 'Agent_id' in session:
        agent_id = session['Agent_id']
        cur = mysql_create_connection()
        cur.execute(
            'SELECT visitor_name, visitor_address, email, phone_number, infected from Visitor')
        visitors = cur.fetchall()
        count = cur.rowcount
        return render_template('Home.html', loggedIn=True, agent_id=agent_id, visitors=visitors, headings=headings, count=count)
    elif 'name' in session:
        return render_template('Home.html', visitor=True, loggedIn=True)
    elif 'Hospital_id' in session:
        return render_template('Home.html', hospital=True, loggedIn=True)
    return redirect(url_for('login'))


@app.route('/login')
@auto.doc()
def login():
    """
    Return the login page to choose Role (Hospital or Agent) passing notLoggedIn to 
    adjust the navigation bar accoridingly.
    """
    return render_template('login.html', notLoggedIn=True)


@app.route('/sign-in', methods=['GET', 'POST'])
@auto.doc()
def login_to_role():
    """
    If roles is submitted from the login form, save the role in a session, and
    return the login page assigned for the role.

    If no role is submitted, redirect to choose a role
    """
    if 'roles' in request.form:
        role = request.form['roles']
        session['loggedInRole'] = role
        return render_template('roleLogin.html', selectedRole=role, notLoggedIn=True)
    return redirect(url_for('login'))


@app.route('/sign-up', methods=['GET', 'POST'])
@auto.doc()
def register_to_role():
    """"
    If roles is submitted from the register form, save the role in a session, and
    return the registeration page assigned for the role.

    If no role is submitted, redirect to choose a role
    """
    if 'roles' in request.form:
        role = request.form.get('roles')
        session['registeredRole'] = role
        return render_template('roleRegister.html', selectedRole=role, notLoggedIn=True)
    return redirect(url_for('register'))


@app.route('/register')
@auto.doc()
def register():
    """
    Return the register page to choose Role (Visitor or Hospital) passing notLoggedIn to 
    adjust the navigation bar accoridingly.
    """
    return render_template('register.html', notLoggedIn=True)


@app.route('/authenticate', methods=['GET', 'POST'])
@auto.doc()
def authenticate_data():
    """
    If Hospital, authenticate input data against data stored in database
        Form Data:
            hospitalsUsername: username input
            hpass: password input
        on success, register session and redirect to home 

    Else If Agent, authenticate input data against data stored in database
        Form Data:
            agentUsername: username input
            apass: password input
        on success, register session and redirect to home

    Otherwise, redirect to login
    """
    if request.method == 'POST' and 'hospitalUsername' in request.form and 'hpass' in request.form:
        username = request.form.get('hospitalUsername')
        password = request.form.get('hpass')
        cur = mysql_create_connection()
        cur.execute(
            "SELECT * FROM Hospital H WHERE H.username = %s COLLATE utf8_bin AND H.password = %s COLLATE utf8_bin", (username, password))
        account = cur.fetchone()
        if account:
            session['loggedin'] = True
            session['username'] = username
            session['Hospital_id'] = account[0]
            return redirect(url_for('home'))
        else:
            return render_template('login.html', invalidData=True, notLoggedIn=True)
    elif request.method == 'POST' and 'agentUsername' in request.form and 'apass' in request.form:
        username = request.form.get('agentUsername')
        password = request.form.get('apass')
        cur = mysql_create_connection()
        cur.execute(
            "SELECT * FROM Agent A WHERE A.username = %s COLLATE utf8_bin AND A.password = %s COLLATE utf8_bin", (username, password))
        account = cur.fetchone()
        if account:
            session['loggedin'] = True
            session['username'] = username
            session['Agent_id'] = account[0]
            return redirect(url_for('home'))
        else:
            return render_template('login.html', invalidData=True, notLoggedIn=True)

    return redirect(url_for('login'))


@app.route('/register/visitor', methods=['GET', 'POST'])
@auto.doc()
def register_visitor_data():
    """
    For Visitor, authenticate input data against database rules
        Form Data:
            name: visitor name input
            email: email input
            number: phone number input
            address: address input
            deviceId = identification for device
            status = infection boolean input
        on success, store in database, register session, and redirect to home 

    Otherwise, redirect to register
    """
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        address = request.form.get('address')
        deviceId = random.randint(1, 2147483647)
        status = False
        if request.form.get('status') == "Positive":
            status = True
        cur = mysql_create_connection()
        try:
            cur.execute(
                'INSERT INTO Visitor(visitor_name, visitor_address, phone_number, email, infected, device_id) VALUES(%s, %s, %s, %s, %s, %s)', (name, address, number, email, status, deviceId))
            mysql.connection.commit()
            cur.close()
            session['name'] = name
            session['email'] = email
            session['number'] = number
            session['address'] = address
            return redirect(url_for('home'))
        except (MySQLdb._exceptions.IntegrityError) as e:
            print(e)
            return render_template('register.html', notLoggedIn=True, invalidData=True)
    return redirect(url_for('register'))


@app.route('/update/profile', methods=['GET', 'POST'])
@auto.doc()
def update_visitor_data():
    """
    For Visitor, check for Data in form and Update databse
        Form Data:
            name: visitor name input
            email: email input
            number: phone number input
            address: address input
        on success, save data in session, and return the updated Visitor profile

    Otherwise, redirect to register
    """
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        address = request.form.get('address')
        cur = mysql_create_connection()
        cur.execute(
            'UPDATE Visitor SET phone_number=%s, visitor_address=%s WHERE visitor_name=%s', [
                number, address, name]
        )
        mysql.connection.commit()
        cur.close()
        session['name'] = name
        session['email'] = email
        session['number'] = number
        session['address'] = address
        return render_template('success.html', loggedIn=True)
    return redirect(url_for('register'))


@app.route('/register/owner', methods=['GET', 'POST'])
@auto.doc()
def register_placeOwner_data():
    """
    For Place owner, authenticate input data against database rules
        Form Data:
            placeName: visitor name input
            placeAddress: address input
        on success, store in database, register session, and redirect to home 

    Otherwise, redirect to register
    """
    if request.method == 'POST':
        placeName = request.form.get('placeName')
        placeAddress = request.form.get('placeAddress')
        cur = mysql_create_connection()
        try:
            cur.execute(
                'INSERT INTO Places(place_name, place_address) VALUES(%s, %s)', (placeName, placeAddress))
            mysql.connection.commit()
            cur.execute(
                "SELECT place_id FROM Places P WHERE P.place_name = %s COLLATE utf8_bin AND P.place_address = %s COLLATE utf8_bin", (placeName, placeAddress))
            account = cur.fetchone()

            if account:
                session['place_id'] = account[0]
                session['place_name'] = placeName
                qr_url = "https://chart.googleapis.com/chart?cht=qr&chl=" + \
                    str(account[0])
            cur.execute(
                'UPDATE Places SET QRcode=%s WHERE place_id=%s', [
                    qr_url, account[0]]
            )
            mysql.connection.commit()
            cur.close()
            return redirect(url_for('home'))
        except (MySQLdb._exceptions.IntegrityError) as e:
            return render_template('register.html', notLoggedIn=True, invalidData=True)
    return redirect(url_for('register'))


@app.route('/profile', methods=['GET'])
@auto.doc()
def profile():
    """
    For Visitor, check for Data in session
        Data:
            vname: visitor name 
            vemail: email 
            vnumber: phone number 
            vaddress: address 
        on success, return the Visitor profile

    Else For Agent, check for username in session
        on success, return the profile

    Else For Hospital, check for username in session
        on success, return the profile

    Else For Place owner, check for place in session
        on success, return the profile

    Otherwise, redirect to login
    """

    if "name" in session and "email" in session and "number" in session and "address" in session:
        vname = session["name"]
        vemail = session['email']
        vnumber = session['number']
        vaddress = session['address']
        return render_template('profile.html', visitor=True, loggedIn=True, user=vname, email=vemail, num=vnumber, add=vaddress)
    elif 'username' in session:
        uname = session['username']
        return render_template('profile.html', loggedIn=True, user=uname)
    elif 'place_name' in session:
        pname = session['place_name']
        return render_template('profile.html', loggedIn=True, user=pname)
    else:
        return redirect(url_for('login'))


@app.route('/logout')
@auto.doc()
def logout():
    """
    Clear all sessions recorded and redirect to login page
    """
    session.clear()
    return redirect(url_for('login'))


@app.route('/docs')
def documentation():
    return auto.html(title='Corona Archive API Documentation', author='Abel')


if __name__ == "__main__":
    app.run()
