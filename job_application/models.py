from django.db import models
from datetime import datetime, date


# Create your models here.
class Status(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title



class Job(models.Model):
    job_id = models.CharField(max_length=10)
    position_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=50)
    
    status = models.ForeignKey(Status,on_delete=models.CASCADE)

    
    appl_submitted= models.DateField(default=datetime.now)
    #appl_submitted = models.DateField(max_length=15)
    #timestamp = models.DateField(auto_now_add=True, auto_now=False, blank=True)
    
    #status= models.CharField(label='What is your favorite fruit?', widget=models.Select(choices=FRUIT_CHOICES))

    # Here goes the date application was submited 
    
