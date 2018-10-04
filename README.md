# Description

gallery is a web application to showcase beautiful pictures. Users get can view photos uploaded by admin. Users can see photos based on the location, by clicking on the listed locations in the menu. They can also copy the link to a photo to paste at their discretion. They can also search for photos based on the categories.

# Features

The home page allows users to see various images:
User can see all images as per location they were taken
Users can also search for images based categories
Admin can upload images from a django dashboard

# Technologies Used

- Python 3.6
- Django MVC framework
- HTML, CSS and Bootstrap
- JavaScript
- Postgressql
- Heroku

# Prerequisite
The gallery project requires a prerequisite understanding of the following:

Django Framework
Python3.6
Postgres
Python virtualenv
Setup and installation
Clone the Repo
Activate virtual environment
Activate virtual environment using python3.6 as default handler virtualenv -p /usr/bin/python3.6 virtual && source virtual/bin/activate

Install dependancies
Install dependancies that will create an environment for the app to run pip3 install -r requirements.txt

Create the Database
- psql
- CREATE DATABASE gallery;
.virtual file
Create .virtual file and paste paste the following filling where appropriate:

SECRET_KEY = '<Secret_key>'
DBNAME = 'gallery'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True
Run initial Migration
python3.6 manage.py makemigrations gallery
python3.6 manage.py migrate
python3.6 manage.py test
Run the app
python3.6 manage.py runserver
Open terminal on localhost:8000
Known bugs
No known bugs so far. If found drop me an email.

Contributors
- Edith Amadi
Contact Information
edithmcamadi5@gmail.com
