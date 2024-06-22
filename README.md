# django-essential-training-app
Learning Django repository

First step to intialize the project was executing:
```
django-admin startproject smartnotes .
```

The word 'smartnotes' stands for the name of the project itself.

# Run the development server
In order the get the application working, we have to execute the following command:
```
python manage.py runserver
```
It'll run the server through the entrypoint 'manage.py' with the settings defined in the file 'settings.py' which is located inside the 'smartnotes' folder.

# Add apps to the project
Although the project was initialized with the name of 'smartnotes', it is possible to manage separated apps within the environment.
Command to create a new app:
```
django-admin startapp home
```
Everytime we create a new app then it has to be added to the settings file of the project. It this case that file is 'smartnotes/settings.py' at the `INSTALLED_APPS` constant.

# Adding views and templates
Views work as some kind of controllers which receive requests and then render a template to finally show to the user.
In order to get a view working, we have to add a new entrypoint in the 'urls.py' file as a url pattern which calls the desired view as a method.

A template is a html file located within a templates folder. A rendering engine uses Django Template Language (DTL) to convert everything to pure html code which can be shown to the user.

# Modularization
A good practice is to keep all apps contained, meaning all their dependencies and necessary resources are in the same app folder. In case of deleting an app, there should not be any errors in the project. Therefore, in the 'urls.py' we use the 'include' function to include the app's 'urls.py' file. That way, if an app is deleted, then it won't break the project.

# ORM and migrations
Each app has a models.py file which contains all the models that are used in the app. The models are used to manage the database tables, records, columns and relationships. The migrations are used to create and manage the database schema.

After creating a new model, it is necessary to make a migration for it. To do so, we have to execute the following command:
```
python manage.py makemigrations
```
And then we have to execute the following command:
```
python manage.py migrate
```
Summarizing, the first command is used to create the instructions or operations for the models and the second command is used to perform the operations in the database.
