# Somnium task

**An complete Django application with Django-Rest**

## Requirements

Python 3.5+, python-pip, virtualenv

## Instalation

First, clone this repository:

    $ git clone https://github.com/turkpenbayev/somnium.git

Install all necessary to run:

    $ pip install -r req.txt

Than, run the application:
    $ python manage.py migrate 
	$ python manage.py runserver 

To see your application, access this url in your browser: 

    http://127.0.0.1:8000/api/profile/
    http://127.0.0.1:8000/api/profile/2 
    http://127.0.0.1:8000/api/department/
    http://127.0.0.1:8000/api/company/

All configuration is in: `test_task/settings.py`
