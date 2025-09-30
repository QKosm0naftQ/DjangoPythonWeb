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

python -m django --version
mkdir atbapi
django-admin startproject atbapi
cd atbapi
python manage.py runserver 9581
```
## Install postgres
```
pip install psycopg2-binary
```