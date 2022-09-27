# README for Corona Archive

## About the Project

Corona Archive is a web service for tracking, displaying, evaluating, and
archiving of the Corona infections in a particular location. The web service will be accessible to
4 types of users:

1. Visitors: Citizens or visitors will use the web service to indicate whether they have
   entered a particular place and when they have done so.
2. Places: Places which are frequently visited by people, such as clubs, pubs, restaurants,
   cinemas etc. will use the web service to get access to a QR code, which uniquely
   identifies their place. Citizens will scan this QR code to record their presence at that
   place.
3. Agency: The agency or the evaluation client will use the web service to generate coronarelated reports by collecting data from the database.
4. Hospital: Hospitals will use the web service to mark people as infected and track anyone else that has been in contact with an infected person.


### Built with

- HTML
- [Flask](https://www.fullstackpython.com/flask.html)
- [Python3](https://www.python.org/download/releases/3.0/)
- [MySQL](https://www.mysql.com/)
- CSS
- [Bootstrap](https://getbootstrap.com/docs/3.4/css/)

## File Structure

```
\--SE-Sprint01-Team32
        \--static
            \--css                  # All the CSS Files used
            \--imgages              # All the images used
        \--templates
            \--                     # Main HTML files
        \--sql
            \--                     # SQL Query used for initialization
        --test_sprint2.py      # Main Testing Python Code
        -- app.py                   # Main Python Code
        -- README.md
        -- requirements.txt         # Required flask dependencies to run this program
        -- .gitignore               # Git ignored files included here
        -- db.yaml                  # MySQL Database credentials included here 
```

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. What things you need to install the software and how to install them.

### Prerequisites

- [Mysql](https://dev.mysql.com/downloads/installer/)
- Flask

```
pip3 install Flask
```

- Virtual Env

```
sudo pip3 install virtualenv
```

## Installation Guide

```bash
# Clone the repo.

# git clone https://github.com/Magrawal17/SE-Sprint01-Team32.git
cd SE-Sprint01-Team32/

# Create virtual environment
$ virtualenv env

# Start virtual environment
$ source env/bin/activate

# Install all the dependencies
$ pip3 install -r requirements.txt

# Open  MySQL
$ mysql -u {ENTER YOUR USERNAME OR ROOT} -p

# Run this command in MYSQL command line to create required database.
mysql> source sql/se_corona.sql
mysql> exit

# Create db.yam file
$ touch db.yaml

# Open db.yaml and enter database credentials in the file format described below
$ nano db.yaml

# Run python server
$ python3 app.py

when running app.py add /home to start surfing on the website
```

### `db.yaml` file Format. Enter your respective credentials

```yaml
mysql_host: "localhost"
mysql_user: "{YOUR USERNAME IN YOUR COMPUTER}"
mysql_password: "{YOUR PASSWORD IN YOUR COMPUTER}"
mysql_db: "seteam32"
```

## Default Hospital and Agent Accounts Created for grading purposes

```
Agent
username: Idris
password: 12345678

username: John
password: asdas1221

Hospital
username: Melina
password: 12345asd

```

# View Documentation

Go to this URL once the server has started. It contains the documentation
of the Flask API routes.

```
http://localhost:5000/docs  

Add /home to access to the website
```

# Run tests

Run this code once you are in the environment to execute the unit-testcases

```sh
$ python3 test_sprint2.py
```

## Sprint 1 Progress achieved

✅ Created requirements.txt file, which includes all the required installation.

✅ Added Hospital login functionality.

✅ Added Agent login functionality.

✅ Added Visitor Registeration functionality.

✅ Added Place Owner Registeration functionality.

✅ Added Profile display and edit data for visitor account.

✅ Added Profile display for Hospital, Agents and Place owners.

✅ Added QR Code display for place owner to track visitors.

✅ QR code resizeability implemented

✅ Added List of Visitors for Agent Account.

✅ Added project installation guide to README.

✅ Added db.yaml to store database credentials.

✅ Created documentation generation infrastructure using Flask-Selfdoc.

✅ Added 19 unittests that should all pass on the first run. 

## Sprint 2 Progress achieved

✅ Fixed bugs related to agent login (sql syntax problem)

✅ Fixed bugs related to visitor registration (sql syntax problem)

✅ Added a feature for the agent so that he can view the list of the visitors and a hospital button for the list of hospitals

✅ Added a filter to the agent so that he can search for the visitors by name or adress or select all(write nothing in the search field just press "search") to see all the visitors

✅ Added a confirm button which directs to a confirmation page (added by us: success2.html) for the place owner when he scans the QR code successfully

✅ Fixed 2 test cases test_login_hospital/agent_account_success which failed by putting the right username

✅ Improved the user interface and added another "agent" into the database for grading criteria (Idris, 12345678)

✅ Organized the file structure by adding some files in gitignore and put the test cases python file outside the folder as a sperate file in order to be run easily in Windows.
