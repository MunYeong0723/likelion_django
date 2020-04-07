from django.contrib import admin
from .models import Blog

# Register your models here.
admin.site.register(Blog) # admin site에 등록함

# superuser username : admintmp123
# pw : admintmp123
