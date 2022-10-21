## Simple App - Flask

<br>

### Requirements

1. Python installed (latest=3.10.7). Get python [here](https://www.python.org/downloads/).
2. Virtual Environment

<br>

### Create virtual environment

1. Use python virtualenv library (Option 1)

```
Install virtualenv library
Command:
pip install virtualenv

Go to your project directory and create virtual environment.
Command:
virtualenv venv

Activate virtualenv:
Command (git bash):
source venv/Scripts/activate

Command (windows cmd):
venv\Scripts\activate
```

2. Use pyenv (Option 2)

```
How to use pyenv?

https://github.com/pyenv/pyenv
```

<br>

Why do we use virtual environment in Python?

Using virtualenv allows you to avoid installing Python packages globally which could break system tools or other projects.

<br>

### Install libraries

```
Make sure you activated your virtual environment.

Command:
pip install -r requirements.txt
```

<br>

### Set up database

Note: <br>
A `sqlite database` will be created inside instance folder. If you want to use different database, refer to [Flask-SQLAlchemy documentation](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/).

```
Command:
flask create_tables
```

<br>

### Running the app

```
Note: Make sure to activate virtual environment first.

Command:
python run.py
```

<br>

### 10 Useful Flask Plugins For Your Python Project

1. Flask-SQLAlchemy
2. Flask-WTF
3. Flask-Mail
4. Flask-RESTFul
5. Flask-Uploads
6. Flask-Debugtoolbar
7. Flask-Login
8. Flask-Admin
9. Flask-Cors
10. Flask-Migrate

Read more on https://python.plainenglish.io/some-useful-python-flask-plugins-3ac57faaca7e

GitHub (awesome flask) - https://github.com/humiaozuzu/awesome-flask
