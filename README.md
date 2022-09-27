# SE-Sprint01-Team32

# README for Corona Archive

### Contributors

Sprint 1

- Abel Berhane Woldemariam
- Anastasiia Skryzhadlovska

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
        \--tests
            |--test_sprint1.py      # Main Testing Python Code
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
mysql> source sql/se_project.sql
mysql> exit

# Create db.yam file
$ touch db.yaml

# Open db.yaml and enter database credentials in the file format described below
$ nano db.yaml

# Run python server
$ python3 app.py

```

### `db.yaml` file Format. Enter your respective credentials

The production process was done on a local MySQL server. This may may work
in CLAMV, however the local server is suggested. 

```yaml
mysql_host: "localhost"
mysql_user: "{YOUR USERNAME IN YOUR COMPUTER}"
mysql_password: "{YOUR PASSWORD IN YOUR COMPUTER}"
mysql_db: "seteam32"
```

## Default Hospital and Agent Accounts Created for grading purposes

```
Agent
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
```

# Run tests

Run this code once you are in the environment to execute the unit-testcases

```sh
$ python3 tests/test_sprint1.py
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


## Acknowledgments

- Special thanks to everyone who helped during the first sprint developement.
