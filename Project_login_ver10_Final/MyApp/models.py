from django.db import models

# Create your models here.
class Job(models.Model):
    job = models.CharField(max_length=50,blank=False, null=False)
    job_description = models.TextField(blank=False, null=False)
    company_name = models.CharField(max_length=50,blank=False, null=False)
    company_description = models.TextField(blank=False, null=False)
    closing_date = models.DateField(auto_now=False, auto_now_add=False,)
    def _str_(self):
        return self.job