from django.db import models


class State(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=5)


class UserRegistration(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=25)
    county = models.CharField(max_length=100)
    state = models.ForeignKey(
        State,
        related_name='states',
        on_delete=models.PROTECT
    )
