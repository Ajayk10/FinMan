from FinManApp.views import inhand
from django.contrib import admin
from . models import *
# Register your models here.

classes = [JointAccountModel,CSBAccountModel,InHandModel,PensionAccountModel,MyAccountModel,TodoList]
admin.site.register(classes)
