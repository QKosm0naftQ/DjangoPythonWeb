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


deactivate # Щоб вийти з віртуального середовища
```

## Нова модель в БД (Приклад Категорія:страви)
python manage.py startapp categories # Створіть додаток categories для роботи з категоріями страв: (це якщо його немає)

'categories'# Відкрийте файл mysite/settings.py і додайте 'categories' до списку INSTALLED_APPS.
    
_# Потім відкрийти файл categories/models.py і створити там клас / це приклад
```
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name
```
python manage.py makemigrations categories # зробити міграцію 
python manage.py migrate # застосувати міграцію

python manage.py shell # Щоб зайти в оболонку і змінити щось в БД

>>>>from categories.models import Category # Імпортувати модель з класу 
### Щоб щось додати
``` 
>>> Category.objects.create(name="Суші")
<Category: Суші>
>>> Category.objects.create(name="Піца")
<Category: Піца>
>>> Category.objects.create(name="Бургери")
<Category: Бургери>
```
### Щоб щось змінити
``` 
>>> burger = Category.objects.get(name="Бургери")

>>> burger.name = "Сендвічі"
>>> burger.save()
```
### Щоб щось видалити
``` 
>>> pizza = Category.objects.get(name="Піца")
>>> pizza.delete()
``` 
### Щоб вивести (другий рядок це результат)
``` 
>>> Category.objects.all()
<QuerySet [<Category: Суші>, <Category: Сендвічі>]>
``` 

## Клонування ПРоекту
```
Можна згрузити список пакетів, який стоїть у .env
.venv\Scripts\activate.bat
pip freeze
pip freeze > requirements.txt

git clone https://github.com/novakvova/DjangoPython_P22
cd DjangoPython_P22
cd 1.SimpleMVT
py -m venv .venv
.venv\Scripts\activate.bat

python.exe -m pip install --upgrade pip
py -m pip install Django
cd djangomvt
py manage.py runserver 4892
```