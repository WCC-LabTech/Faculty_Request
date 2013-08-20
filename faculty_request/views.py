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
    requests = models.requests(
            faculty_Name = User.objects.get(id=post["faculty_Name"]),
            labtech_Name = User.objects.get(id=post['labtech_Name']),
            subject = post['subject'],
            description = post['description'],
            due_date = post['due_date'],
            request_Type = post['request_Type'],
            request_status = 'Pending',
    )
    try:
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



@csrf_exempt
@require_http_methods(['POST'])
def request_update(request):
	post = request.POST
	requests= models.requests.objects.get(id=post['id'])
	requests.labtech_Name=User.objects.get(id=post["labtech_Name"])
	requests.request_status=post['request_status']


	try:
		requests.save()
		data={'data': 'Request Updated'}
		code=200

	except:
		data={'message':'request not updated'}
		code=400
	return HttpResponse(simplejson.dumps(data), status=code)
		
	



















