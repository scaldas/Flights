from django.db import models

# Create your models here.

class Flight(models.Model):
    schedule = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    airline = models.CharField(max_length=200)

    def __str__(self):
        return self.airline + " " + self.schedule

# python manage.py makemigrations SubTitlesApp
# python manage.py sqlmigrate SubTitlesApp 0001
# python manage.py migrate
# $ heroku run python manage.py migrate