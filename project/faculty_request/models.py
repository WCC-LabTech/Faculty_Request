from django.db import models
from django.contrib.auth.models import User

request_type= (
('RM','Room'),
('EQ', 'Equipment'),
('CG','Configure'),
('LB','Labs'),
('OT','Other'),
)
request_status=(
('pd','Pending'),
('rv','Approved'),
('dl','Delegated'),
('cp','Completed'),
)
class	request(models.Model):
        faculty_Name= models.ForeignKey(User,related_name='+')
        labtech_Name=models.ForeignKey(User,related_name='+')
        uploaded= models.FileField(upload_to='./uploads', blank=True,)
	subject=models.CharField(max_length=100)
	description=models.TextField()
	issued_date=models.DateTimeField(auto_now_add=True)
	due_date=models.DateTimeField(auto_now_add=False)
 	request_Type=models.CharField(max_length=2, choices=request_type, default='other')
        request_status=models.CharField(max_length=2,choices=request_status,default='Pending')     
	def __unicode__(self):
		return unicode(self.subject)
# Create your models here.
