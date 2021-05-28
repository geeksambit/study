from django.db import models

# Create your models here.

class Class(models.Model):
    class_name = models.CharField(verbose_name='Name', max_length=52, unique=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(self.class_name)

