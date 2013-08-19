from django.contrib.auth.models import User,Group
#from rest_framework import viewsets
#from faculty_request.serializers import faculty_Serializer,admin_Serializer,labtech_Serializer
from faculty_request import models
from django.http import HttpResponse
from django.core import serializers 

'''class faculty_view(viewsets.ModelViewSet):
	queryset=request.objects.all()
	serializer_class=faculty_Serializer



class admin_view(viewsets.ModelViewSet):
        queryset=request.objects.all()
        serializer_class=admin_Serializer




class labtech_view(viewsets.ModelViewSet):
        queryset=request.objects.all()
        serializer_class=labtech_Serializer;'''







def admin_view(request):
	faculty= models.requests.objects.all()
	data = serializers.serialize('json', faculty)
	return HttpResponse(data, mimetype = 'application/json')
