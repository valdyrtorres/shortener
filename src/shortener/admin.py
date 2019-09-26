from django.contrib import admin

# Register your models here.
from .models import KirrURL

admin.site.register(KirrURL)

'''
Sempre que alterar, execute
python manage.py makemigrations
python manage.py migrate

'''