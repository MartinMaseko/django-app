# Candidate Django Application
This is a django application for a candidate with a HTML template 
that uses bootstrap and has data driven compenents to store volunteers
and has a registration feature.

## Installation

### Prerequisites

Python 3.x (Specify the required version)
### Dependencies
* black==24.10.0
* click==8.1.7
* colorama==0.4.6
* flake8==7.1.1
* mccabe==0.7.0
* mypy-extensions==1.0.0
* packaging==24.2
* pathspec==0.12.1
* platformdirs==4.3.6
* pycodestyle==2.12.1
* pyflakes==3.2.0

### Instructions
1. Clone the repository
* git clone https://github.com/MartinMaseko/django-app.git

2. Install dependencies
* pip install -r requirements.txt

## Usage
* python manage.py runserver
* Access the application in your web browser at http://localhost:8000

## steps necessary to build and run application

### Activate the Virtual Environment

### Windows

myenv\Scripts\activate

### macOS/Linux:
myenv/bin/activate

### Install Dependencies

pip install -r requirements.txt

### Build the Docker Image

docker build -t django-app.

### Run the Application

docker run -p 8000:8000 django-app


## Features
* HTML
* Bootstrap
* Django authentication
* db.sqlite3

## Martin Maseko