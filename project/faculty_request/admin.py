from django.contrib import admin
from faculty_request.models import request,Name 




class request_admin(admin.ModelAdmin):
	list_display = ('name', 'subject','issued_date','due_date')
	list_filter=('name',)
	search_field=['subject','name']

   
admin.site.register(request,request_admin ) 
admin.site.register(Name)      
