from django.db import models

# Create your models here.

class JointAccountModel(models.Model):
    date_time  = models.CharField(max_length=200 ,null=True)
    available_balance =  models.CharField(max_length=200 ,null=True)
    amount = models.IntegerField(null=True)
    title =  models.CharField(max_length=200 ,null=True)
    description =  models.TextField(null=True)
    month = models.CharField(max_length=200 ,blank=True)
    year = models.CharField(max_length=200 ,blank=True)

    def __str__(self):
        return self.available_balance
    
class InHandModel(models.Model):
    date_time  = models.CharField(max_length=200 ,null=True)
    available_balance =  models.CharField(max_length=200 ,null=True)
    amount = models.IntegerField(null=True)
    title =  models.CharField(max_length=200 ,null=True)
    description =  models.TextField(null=True)
    month = models.CharField(max_length=200 ,blank=True)
    year = models.CharField(max_length=200 ,blank=True)

    def __str__(self):
        return self.available_balance

class PensionAccountModel(models.Model):
    date_time  = models.CharField(max_length=200 ,null=True)
    available_balance =  models.CharField(max_length=200 ,null=True)
    amount = models.IntegerField(null=True)
    title =  models.CharField(max_length=200 ,null=True)
    description =  models.TextField(null=True)
    month = models.CharField(max_length=200 ,blank=True)
    year = models.CharField(max_length=200 ,blank=True)

    def __str__(self):
        return self.available_balance

class CSBAccountModel(models.Model):
    date_time  = models.CharField(max_length=200 ,null=True)
    available_balance =  models.CharField(max_length=200 ,null=True)
    amount = models.IntegerField(null=True)
    title =  models.CharField(max_length=200 ,null=True)
    description =  models.TextField(null=True)
    month = models.CharField(max_length=200 ,blank=True)
    year = models.CharField(max_length=200 ,blank=True)

    def __str__(self):
        return self.available_balance

class MyAccountModel(models.Model):
    date_time  = models.CharField(max_length=200 ,null=True)
    available_balance =  models.CharField(max_length=200 ,null=True)
    amount = models.IntegerField(null=True)
    title =  models.CharField(max_length=200 ,null=True)
    description =  models.TextField(null=True)
    month = models.CharField(max_length=200 ,blank=True)
    year = models.CharField(max_length=200 ,blank=True)

    def __str__(self):
        return self.available_balance
    
   class TodoList(models.Model):
    goal_year = models.CharField(max_length=200 ,null=True)
    description =  models.CharField(max_length=200 ,null=True)
    accomplished_year =  models.CharField(max_length=200 ,null=True)
    accomplished = models.BooleanField(default=False)
    def __str__(self):
        return self.description
