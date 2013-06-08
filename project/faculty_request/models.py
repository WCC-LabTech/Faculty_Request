from django.db import models

class Name(models.Model):
	first_name=models.CharField(max_length=20, unique=True)
	last_name=models.CharField(max_length=20,unique=True)
	def __unicode__(self):
		return unicode(self.first_name+ ' ' +self.last_name)

class	request(models.Model):
	#first_name=models.CharField(max_length=20)
	#last_name=models.CharField(max_length=20)
	name= models.ForeignKey(Name)
	subject=models.CharField(max_length=100)
	description=models.TextField()
	issued_date=models.DateTimeField(auto_now_add=True)
	due_date=models.DateTimeField()
	def __unicode__(self):
		return unicode(self.subject)

# Create your models here.
