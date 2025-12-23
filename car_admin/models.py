from django.db import models

class Service(models.Model):
    ser_icon=models.CharField(max_length=200)
    ser_title=models.CharField(max_length=200)
    ser_desc=models.TextField()
    
# Create your models here.

# creat hero form
class HeroForm(models.Model):
    car_type=models.CharField(max_length=200)
    pickup_location=models.CharField(max_length=200)
    drop_location=models.CharField(max_length=200)
    pickup_date=models.DateField()
    pickup_time=models.TimeField()
    drop_date=models.DateField()
    drop_time=models.TimeField()



# Creat Numbering section
class Numbering(models.Model): 
    num_icon=models.CharField(max_length=200)
    num_counter=models.CharField(max_length=200)
    num_title=models.TextField()

# #creat cental process

class Centalprocess(models.Model):
    pro_title=models.CharField(max_length=200)
    pro_number=models.CharField(max_length=200)
    pro_desc=models.CharField()


#  #creat cental features

class Centalfeatures(models.Model):
    feat_icon=models.CharField(max_length=200)
    feat_title=models.CharField(max_length=200)
    feat_desc=models.TextField() 

# #creat cental blog & news

class Blog(models.Model):
    blog_image=models.ImageField(upload_to='media/',null=True,blank=True)
    blog_date=models.DateField(max_length=200)
    blog_authorname=models.CharField(max_length=200)
    blog_comment=models.CharField(max_length=200) 
    blog_title=models.CharField(max_length=200)
    blog_desc=models.TextField() 
   

# #creat Vehicle Categories

class Cat(models.Model):
    cat_image=models.ImageField(upload_to='media/',blank=True, default='images/car-2.png')
    cat_title=models.CharField(max_length=200)
    cat_rate=models.CharField(max_length=200)
    
 #creat client reviews

class Reviews(models.Model):
    review_image=models.ImageField(upload_to='media/',blank=True, default='images/car-3.png')
    review_title=models.CharField(max_length=200)
    review_icon=models.CharField(max_length=200)
    review_desc=models.CharField()
   

#  #creat contact form

class contactsform(models.Model):
    your_name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    your_phone=models.CharField(max_length=200)
    your_projects=models.CharField(max_length=200)
    subjects=models.CharField(max_length=200)
    msg=models.TextField()
   
