# Simple MVT api 
```
python --version
python -m venv .venv

```
## Activate venv
```
deactivate
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install Django

python -m django --version
mkdir atbapi
django-admin startproject atbapi
cd atbapi
python manage.py runserver 4099
```
## Install postgres
```
pip install psycopg2-binary
```
## Створення користувачі
```
python manage.py shell
>>from django.contrib.auth.models import User
>>User.objects.create_user(username='user1', password='pass123')
```
## Add CustomUser
```
python manage.py startapp users
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```