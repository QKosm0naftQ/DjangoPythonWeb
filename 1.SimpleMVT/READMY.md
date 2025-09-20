# Simple MVT
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
python
in console:
>>>import django
>>>print(django.get_version())
>>>quit()

python -m django --version
mkdir djangomvt
django-admin startproject mysite djangomvt
cd djangomvt
python manage.py runserver 9581
python manage.py startapp categories

python manage.py makemigrations   # створює файли міграцій для змін у моделях # шукати де є проект django
python manage.py migrate          # застосовує міграції до бази даних

python manage.py startapp users


deactivate - for leave from console 
```