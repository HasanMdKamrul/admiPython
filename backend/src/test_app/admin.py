from django.contrib import admin

from .models import ModelX, ModelY, TestApi

# Register your models here.

admin.site.register(TestApi)
admin.site.register(ModelX)
admin.site.register(ModelY)
