# Candidate Django Application

This Django application features:

* HTML templates with Bootstrap styling
* Data-driven components for managing volunteers
* User registration with Django authentication
* SQLite database backend

## Installation and Setup

**Prerequisites:**

- Python 3.9.10

**Steps:**

1. **Clone the Repository:**
   git clone [https://github.com/MartinMaseko/django-app.git]

2. **Activate Virtual Environment**

    myenv\Scripts\activate

3. **Install Dependencies**

    pip install -r requirements.txt

4. **Build the Docker Image**

    **Optional**
    If you're starting a new database or have made changes to models, 
    run these commands:

    python manage.py makemigrations mayor
    
    python manage.py migrate

    docker build -t django-app .

5. **Run the Application**

    docker run -p 8000:8000 django-app

    Access the application in your web browser at http://localhost:8000.

## Features
* HTML
* Bootstrap
* Django authentication
* db.sqlite3

## Martin Maseko
