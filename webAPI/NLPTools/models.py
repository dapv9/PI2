# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.db import models
import string



# Create your models here.


class Post(models.Model):
    writter = models.CharField(max_length=15)
    text = models.TextField()
    token = models.TextField()
    words = models.TextField()
    

    def texto(txt):
            txt.save()

    def __str__(txt):
            return txt.text