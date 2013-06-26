from  django.contrib.auth.models import User,Group
from rest_framework import serializers
from faculty_request.models import request


class admin_Serializer(serializers.ModelSerializer):
	class Meta:
		model=request
		fields=('faculty_Name','labtech_Name','uploaded','subject','description','issued_date','due_date','request_Type','request_status', )


class faculty_Serializer(serializers.ModelSerializer):
	class Meta:
		model=request
		field=('faculty_Name','uploaded','subject','description','issued_date','due_date','request_Type','request_status',)




class labtech_Serializer(serializers.ModelSerializer):
	class Meta:
		model=request
		field=('faculty_Name','labtech_Name','uploaded','subject','description','issued_date','due_date','request_Type','request_status',)


