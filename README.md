# Student-Journal
Mini test task with Django 3.

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
