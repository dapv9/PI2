# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.db import models
import nltk

nltk.download('book')


# Create your models here.


class Post(models.Model):
    writter = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    token = models.CharField(max_length=500)

    def texto(txt):
            txt.save()

    def __str__(txt):
            return txt.token
    
    def tokenizer(txt):
	        txt.token = nltk.Text(nltk.word_tokenize(txt.text))
	        return txt

    def tagging(tokenizelist):
	        tag = nltk.pos_tag(tokenizelist)
	        return tag
