from django.db import models

class Todo(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  task =models.CharField(max_length=255)
  coment =models.CharField(max_length=255)

class Users(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  email = models.CharField(max_length=255)

