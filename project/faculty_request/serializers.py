from  django.contrib.auth.models import User,Group
from rest_framework import serializers
from faculty_request.models import requests


class admin_Serializer(serializers.ModelSerializer):
	class Meta:
		model=requests
		fields=('id','faculty_Name','labtech_Name','uploaded','subject','description','issued_date','due_date','request_Type','request_status', )


class faculty_Serializer(serializers.ModelSerializer):
	class Meta:
		model=requests
		field=('id','faculty_Name','uploaded','subject','description','issued_date','due_date','request_Type','request_status',)




class labtech_Serializer(serializers.ModelSerializer):
	class Meta:
		model=requests
		field=('id','faculty_Name','labtech_Name','uploaded','subject','description','issued_date','due_date','request_Type','request_status',)


