from  django.contrib.auth.models import User,Group
from rest_framework import serializers
from faculty_request.models import request


class admin_Serializer(serializers.ModelSerializer):
	class Meta:
		model=request
		fields=('id','faculty_Name','labtech_Name','docfile','subject','description','issued_date','due_date','request_Type','request_status', )


class faculty_Serializer(serializers.ModelSerializer):
	class Meta:
		model=request
		field=('id','faculty_Name','docfile','subject','description','issued_date','due_date','request_Type','request_status',)




class labtech_Serializer(serializers.ModelSerializer):
	class Meta:
		model=request
		field=('id','faculty_Name','labtech_Name','docfile','subject','description','issued_date','due_date','request_Type','request_status',)


