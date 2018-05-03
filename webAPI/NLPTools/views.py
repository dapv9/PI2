# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect

from .models import Post
from .forms import PostForm
from nltk import word_tokenize, ne_chunk
from nltk.tag import pos_tag, map_tag, str2tuple
from nltk.tree import Tree
from nltk.draw.tree import TreeView
import os
import json


# Create your views here.

def post_list(request):
	posts = Post.objects.all().order_by('id')

   	return render(request, 'NLPTools/post_list.html', {'posts':posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)

	return render(request, 'NLPTools/post_detail.html', {'post': post})

def post_new(request):
	
	if request.method == "POST":
		form=PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			print(post)
			post.writter = request.user
			post.token = ne_chunk(pos_tag(word_tokenize(post.text)))
			post.words = str(post.toke).replace('(',' ').replace(')','').replace('/',' ')
			#t = Tree.fromstring(str(post.token))
			#TreeView(t)._cframe.print_to_file('NLPTools/images/tree.ps')
			#os.system('convert NLPTools/images/tree.ps NLPTools/images/tree.png')
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
		return render(request,'NLPTools/post_edit.html',{'form':form})

def post_edit(request, pk):
   			post = get_object_or_404(Post, pk=pk)
			if request.method == "POST":
				form = PostForm(request.POST, instance=post)
				if form.is_valid():
						post.writter = request.user
						post = form.save(commit=False)
						post.token = ne_chunk(pos_tag(word_tokenize(post.text)))
						post.words = str(post.token).replace('(',' ').replace(')','').replace('/',' ')
						post.save()
						return redirect('post_detail', pk=post.pk)
			else:
				form = PostForm(instance=post)
				return render(request, 'NLPTools/post_edit.html', {'form': form})