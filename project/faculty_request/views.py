from django.views.decorators.csrf import csrf_exempt
from django.utils import simplejson
from django.http import HttpResponse
from django.contrib.auth.models import User,Group
#from rest_framework import viewsets
#from faculty_request.serializers import faculty_Serializer,admin_Serializer,labtech_Serializer
from faculty_request import models
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.http import require_http_methods 

'''class faculty_view(viewsets.ModelViewSet):
	queryset=request.objects.all()
	serializer_class=faculty_Serializer



class admin_view(viewsets.ModelViewSet):
        queryset=request.objects.all()
        serializer_class=admin_Serializer




class labtech_view(viewsets.ModelViewSet):
        queryset=request.objects.all()
        serializer_class=labtech_Serializer;'''

@csrf_exempt
@require_http_methods(['POST'])
def request_save(request):
    post = request.POST
    try:
        requests = models.requests(
            faculty_Name = post['faculty_name'],
            labtech_Name = post['tech_name'],
            subject = post['subject'],
            description = post['description'],
            issued_date = post['issued_date'],
            due_date = post['due_date'],
            request_Type = post['request_type'],
            request_status = post['request_status'],
        )
        requests.save()
        data = {'data': 'Request Created'}
        code = 201
    except:
        data = {'message': 'Request not saved'}
        code = 400
    return HttpResponse(simplejson.dumps(data), status=code)


	




def admin_view(request):
	faculty= models.requests.objects.all()
	data = serializers.serialize('json', faculty)
	return HttpResponse(data, mimetype = 'application/json')
