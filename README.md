# Student-Journal
Mini test task with Django 3.

REST API for a client application that should display a page with a list of 
students with the following capabilities: 
1. Add a new student to this list. 
1. Delete an existing student. 
1. Edit an existing student. 

The student has the following fields: 
* Full name. 
* Date of birth. 
* Academic.
 
## System requirements: 
* Python 3.8
* PostgreSQL 12

## For start project
1. ```docker-compose up```
1. ```./manage.py migrate```
1. ```./manage.py collectstatic --no-input``` twice

### For development workflow
1. Add file settings to ```project/settings/local.py```
Example for file in ```project/settings/example.py``` and 
run ```./manage.py runserver --settings=settings.local```

## For start test 
```./manage.py test  --no-input --keepdb```
