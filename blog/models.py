# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
	author = models.ForeignKey(User)
	title = models.CharField(max_length=512)
	content = models.TextField()
	published = models.DateTimeField(blank=True,null=True)
	published_state = models.BooleanField(default=False,blank=True)
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)