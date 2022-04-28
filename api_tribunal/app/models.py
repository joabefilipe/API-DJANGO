# -*- coding: utf-8 -*-
from django.db import models

class Music(models.Model):
    
    class Meta:

        db_table = 'music'
    
    title = models.CharField(max_length=200)
    seconds = models.IntegerField()

    def __str__(self):
        return self.title

# Create your models here.
