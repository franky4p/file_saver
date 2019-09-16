"""
Definition of models.
"""

from django.db import models


class Record(models.Model):
    name = models.CharField(max_length=200)
    file = models.FileField(upload_to='storage/%Y/%m/%d/')