"""
1. pip install django
2. pip install djangorestframework
3. start a django project by - django-admin startproject demo
4. create an app inside it by - python manage.py startapp webapp


STEPS FOR RUNNINF ANY GENERAL DJANGO app
- configure INSTALLED_APPS in settings
  add 'rest_framework'
  add 'webapp'

- creat a model(databse basically )
- register the model in admin.py
- migrate using commands
  'python manage.py makemigrations'
  'python manage.py migrate'
  'python manage.py createsuperuser'
- run the app using 'python manage.py runserver'

- Check configured URLS and hit the corresponding address
- Download and install Postman
- paste the 'data-generating' URL into the postman GET request and hit it
- get the data on the postman console

- This, shows using this URL we can call th ecorresponding REST api from any Device 
"""
