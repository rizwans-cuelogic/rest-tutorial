# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests
import json
from django.shortcuts import render
from blog.serializers import UserSerializer,BlogSerializer
from blog.models import Blog
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework import status
from .helpers import generate_jwt_token
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


# Create your views here.

class BlogList(generics.ListCreateAPIView):

	permission_classes = (permissions.IsAuthenticated,)
	queryset = Blog.objects.all()
	serializer_class = BlogSerializer

	def post(self,request,format=None,**kwargs):

		import pdb
		pdb.set_trace()

		data = request.data

		data['author'] = self.request.user.id

		serializer = BlogSerializer(data = data)

		if serializer.is_valid():

			serializer.save()
			return Response({"blog":serializer.data})				

class BlogDetail(generics.RetrieveUpdateDestroyAPIView):

	permission_classes = (permissions.IsAuthenticated,)
	queryset = Blog.objects.all()
	serializer_class = BlogSerializer



class UserList(generics.ListCreateAPIView):

	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
	
	queryset = User.objects.all()
	serializer_class = UserSerializer
	

class LoginView(APIView):


	def post(self,request,format=None):
		

		if request.data:

			data = request.data

			username = data.get('username')
			password = data.get('password')

			if username is None or password is None:

				return Response(status = status.HTTP_400_BAD_REQUEST)

			user = User.objects.filter(username = username)

			if not user:

				return Response(status = status.HTTP_400_BAD_REQUEST)


			token = generate_jwt_token(self,username,password)

			if token.status_code != 200:
				return Response({'msg': 'Username or password is incorrect'},
								status=status.HTTP_412_PRECONDITION_FAILED)

			serializer = UserSerializer(user[0])

			return Response({"Success":True,
							"token": json.loads(token._content),
							"user": serializer.data
						})
					


