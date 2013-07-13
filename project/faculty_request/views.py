from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from faculty_request.serializers import faculty_Serializer,admin_Serializer,labtech_Serializer
from faculty_request.models import request
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from faculty_request.models import request
from faculty_request.forms import DocumentForm
def list(req):
    # Handle file upload
    if req.method == 'POST':
        form = DocumentForm(req.POST, req.FILES)
        if form.is_valid():
            newdoc = request(docfile= req.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('faculty_request.views.list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = request.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'project/list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(req)
    )

class faculty_view(viewsets.ModelViewSet):
	queryset=request.objects.all()
	serializer_class=faculty_Serializer



class admin_view(viewsets.ModelViewSet):
        queryset=request.objects.all()
        serializer_class=admin_Serializer




class labtech_view(viewsets.ModelViewSet):
        queryset=request.objects.all()
        serializer_class=labtech_Serializer
