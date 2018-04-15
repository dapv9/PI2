# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#from django.utils import timezone

# Create your models here.


class Post(models.Model):
	writter = models.ForeignKey('auth.User', on_delete=models.CASCADE)
        text = models.CharField(max_length=300)

        def frase(txt):
            txt.save()

        def __str__(txt):
            return txt.text
