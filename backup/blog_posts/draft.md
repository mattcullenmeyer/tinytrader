## Start Project
- $ mkdir multiverse && cd multiverse
- $ code .
- $ pip3 install virtualenv
- $ virtualenv venv --python=python3
- $ source venv/bin/activate  (this activates the virtual environment; exit with deactivate) 
- $ pip3 install django
- $ pip3 freeze > requirements.txt
- $ django-admin startproject config .
- Delete db.sqlite3
- $ python manage.py runserver
- $ git init  (I've already configured)
- $ git add .
- $ git commit -m "Started django project"

## Setup Environmental Variables
- $ python manage.py shell 
  - from django.core.management.utils import get_random_secret_key
  - print(get_random_secret_key())
- avoid dollar signs 
- $ touch .env
- SECRET_KEY=up_j%pqh#q1-v&h2$7up2zys4)k=12hrg$ok#pw23vvy*dvt^v
- add python-dotenv==0.19.2 to requirements.txt
- $ pip3 install -r requirements.txt
- config/settings.py
  - import os
  - from dotenv import load_dotenv
  - load_dotenv()
- $ python manage.py runserver
- DEBUG=True  (add to .env)
- DEBUG = os.getenv('DEBUG', False)  (add to settings.py)

## GitHub Repo
- Create a new repo on GitHub
- $ touch .gitignore
- https://www.toptal.com/developers/gitignore (django visualstudiocode)
- $ git branch -M main
- $ git branch  (check it's there)
- $ git remote add origin git@github.com:mattcullenmeyer/multiverse.git
- $ git push -u origin main