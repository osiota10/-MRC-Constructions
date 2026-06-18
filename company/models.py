from django.db import models

# Create your models here.

class heroContent(models.Model):
    text = models.CharField(max_length=200)
    paragraph = models.CharField(max_length=200)
    video_file = models.FileField(upload_to='uploads', blank=True, null=True)

class whatWeDo(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)

class whatWeDoContent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_file = models.ImageField(upload_to='uploads', blank=True, null=True)

class WhoWeAre(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_file = models.ImageField(upload_to='uploads', blank=True, null=True)
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)

class WhoWeAreStats(models.Model):
    digit = models.IntegerField()
    name = models.CharField(max_length=200)  

class OurServices(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()


class OurServicesList(models.Model):  
    image_file = models.ImageField(upload_to='uploads', blank=True, null=True) 
    name = models.CharField(max_length=200)

class OurProjects(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_file = models.ImageField(upload_to='uploads', blank=True, null=True) 

class OurClients(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    image_file = models.ImageField(upload_to='uploads', blank=True, null=True) 

# OTHER PAGES ON THE WEBSITE

class ServicePage(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()

class ServicePageContent(models.Model):
    image_file = models.ImageField(upload_to='uploads', blank=True, null=True) 
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_file = models.ImageField(upload_to='uploads', blank=True, null=True) 

class ProjectPage(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_file = models.ImageField(upload_to='uploads', blank=True, null=True) 

class AboutUsPage(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    image_file = models.ImageField(upload_to='uploads', blank=True, null=True) 

class AboutUsPageContent(models.Model):
    header = models.CharField(max_length=200)
    description = models.TextField()
    title = models.CharField(max_length=200)
    description = models.TextField()

class AboutUsPageContentTwo(models.Model):
    image_file = models.ImageField(upload_to='uploads', blank=True, null=True) 
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()

class CareerPage(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)

class CareerPageContent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

class ContactPage(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()
    


class ContactPageImg(models.Model):
    image_file = models.ImageField(upload_to='uploads', blank=True, null=True) 
















    



