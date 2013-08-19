from django.db import models
from django.contrib.auth.models import User



ROOM='Room'
EQUIPMENT= 'Equipment'
CONFIGURE='Configure'
LABS='Labs'
OTHER='Other'
PENDING='Pending'
APPROVED='Approved'
DELEGATED='Delegated'
COMPLETED='Completed'


request_type= (
(ROOM,'Room'),
(EQUIPMENT, 'Equipment'),
(CONFIGURE,'Configure'),
(LABS,'Labs'),
(OTHER,'Other'),
)
request_status=(
(PENDING,'Pending'),
(APPROVED,'Approved'),
(DELEGATED,'Delegated'),
(COMPLETED,'Completed'),
)
class	requests (models.Model):
        faculty_Name= models.ForeignKey(User,related_name='+')
        labtech_Name=models.ForeignKey(User,related_name='+',blank=True,null=True,)
        uploaded= models.FileField(upload_to='documents/%Y/%m/%d', blank=True,)
	subject=models.CharField(max_length=100)
	description=models.TextField()
	issued_date=models.DateTimeField(auto_now_add=True)
	due_date=models.DateField()
 	request_Type=models.CharField(max_length=20, choices=request_type, default=OTHER)
        request_status=models.CharField(max_length=20,choices=request_status,default=PENDING)     
	def __unicode__(self):
		return unicode(self.subject)
# Create your models here.
