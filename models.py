from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomerModel(AbstractUser):

    USER =[
        ('Recruiter','Recruiter'),
        ('JobSeeker','JobSeeker'),
    ]


    user_type = models.CharField(choices=USER, max_length=50)
    display_name =models.CharField(null=True, max_length=50)


class SkillModel(models.Model):
    name = models.CharField(max_length=50,unique=True)
    
    def __str__(self):
        return self.name or "No Skills"

class RceuiterModel(models.Model):
    user = models.OneToOneField(CustomerModel, on_delete=models.CASCADE)
    company = models.CharField(null=True, max_length=50)
    address = models.TextField(null=True)
    contarct = models.CharField(null=True, max_length=50)
    skill = models.CharField(null=True, max_length=50)
    image = models.ImageField(null=True, upload_to='media/image')


class JobSeekerModel(models.Model):
    user = models.OneToOneField(CustomerModel, on_delete=models.CASCADE)
    name = models.CharField(null=True, max_length=50)
    address = models.TextField(null=True)
    contract = models.CharField(null=True, max_length=50)  # Tip: Did you mean 'contact'?
    skill_set = models.CharField(null=True, max_length=50)
    
    # --- FIXED PATHS HERE ---
    image = models.ImageField(null=True, upload_to='images/')
    resume = models.FileField(null=True, upload_to='resumes/')


class JobPostModel(models.Model):

    Category =[
        ('Full Time','Full Time'),
        ('Half Time','Half Time'),
        ('Remote','Remote'),

    ]

    user = models.ForeignKey(CustomerModel, on_delete=models.CASCADE)
    titel = models.CharField(null=True, max_length=50)
    number_openig = models.CharField(null=True, max_length=50)
    category = models.CharField(null=True, max_length=50)
    discription = models.TextField(null=True)
    skill = models.CharField(null=True, max_length=50)



class AppliedJobModel(models.Model):

    STATUS = [
        ('Pendin','Pendin'),
        ('Shorlist','Shorlist'),
        ('Reject','Reject'),

    ]

    job_seeker = models.ForeignKey(JobSeekerModel, on_delete=models.CASCADE)
    job = models.ForeignKey(JobPostModel, on_delete=models.CASCADE)
    status = models.CharField(null=True, max_length=50)

    
    
