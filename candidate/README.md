# Candidate Django Application
This is a django application for a candidate with a HTML template 
that uses bootstrap and has data driven compenents to store volunteers
and has a registration feature.

## Installation

### Prerequisites

Python 3.x (Specify the required version)
### Dependencies
* alabaster==1.0.0
* asgiref==3.8.1
* babel==2.16.0
* black==24.10.0
* certifi==2024.8.30
* charset-normalizer==3.4.0
* click==8.1.7
* colorama==0.4.6
* Django==5.1.3
* docutils==0.21.2
* flake8==7.1.1
* idna==3.10
* imagesize==1.4.1
* importlib_metadata==8.5.0
* jaraco.classes==3.4.0
* jaraco.context==6.0.1
* jaraco.functools==4.1.0
* Jinja2==3.1.4
* keyring==25.5.0
* markdown-it-py==3.0.0
* MarkupSafe==3.0.2
* mccabe==0.7.0
* mdurl==0.1.2
* more-itertools==10.5.0
* mypy-extensions==1.0.0
* nh3==0.2.18
* packaging==24.2
* pathlib==1.0.1
* pathspec==0.12.1
* pkginfo==1.11.2
* platformdirs==4.3.6
* pprintpp==0.4.0
* pycodestyle==2.12.1
* pyflakes==3.2.0
* Pygments==2.18.0
* pyinit==0.0.8
* pywin32-ctypes==0.2.3
* readme_renderer==44.0
* requests==2.32.3
* requests-toolbelt==1.0.0
* rfc3986==2.0.0
* rich==13.9.4
* setuptools==75.5.0
* snowballstemmer==2.2.0
* Sphinx==8.1.3
* sphinx-autodoc-typehints==2.5.0
* sphinx-rtd-theme==3.0.2
* sphinxcontrib-applehelp==2.0.0
* sphinxcontrib-devhelp==2.0.0
* sphinxcontrib-django==2.5
* sphinxcontrib-htmlhelp==2.1.0
* sphinxcontrib-jquery==4.1
* sphinxcontrib-jsmath==1.0.1
* sphinxcontrib-qthelp==2.0.0
* sphinxcontrib-serializinghtml==2.0.0
* sqlparse==0.5.2
* twine==5.1.1
* tzdata==2024.2
* urllib3==2.2.3
* wheel==0.45.0
* zipp==3.21.0

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