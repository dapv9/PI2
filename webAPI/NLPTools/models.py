# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.db import models
import string



# Create your models here.


class Post(models.Model):
    writter = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField(max_length=2000)
    token = models.TextField(max_length=2500)
    words = models.TextField()
    

    def texto(txt):
            txt.save()

    def __str__(txt):
            return txt.text