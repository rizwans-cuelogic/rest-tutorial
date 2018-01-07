from rest_framework import serializers
from blog.models import Blog
from django.contrib.auth.models import User
from django.db import models


class UserSerializer(serializers.ModelSerializer):

	class Meta:

		model  = User
		fields = ('id','username','email','password')


	def create(self, validated_data):
		user = User(email= validated_data['email'],
					username = validated_data['username'],
					is_active =True
				)

		user.set_password(validated_data['password'])
		user.save()
		return user

class BlogSerializer(serializers.ModelSerializer):		

	class Meta:

		model = Blog
		fields = ('id','title','content','published','timestamp','author')

class BlogSerializerview(serializers.ModelSerializer):		

	#author = serializers.StringRelatedField(read_only=True)
	#author = serializers.PrimaryKeyRelatedField(read_only=True)
	author = serializers.HyperlinkedRelatedField(read_only=True,view_name="blog:users-detail")
	class Meta:

		model = Blog
		fields = ('id','title','content','published','timestamp','author')

class BlogSerializerv(serializers.HyperlinkedModelSerializer):		

	url = serializers.HyperlinkedIdentityField(view_name="blog:blogs-detail",lookup_field="pk")
	author = UserSerializer()
	class Meta:

		model = Blog
		fields = ('url','id','title','content','published','timestamp','author')

	