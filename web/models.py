from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    name =models.CharField(max_length=150)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    tags = models.ManyToManyField(Tag)
    pub_date = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.title


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    services = models.CharField(max_length=50)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    
# class Subscribe(models.Model):
#     email = models.CharField(max_length=120)

#     def _str_(self):
#             return str(self.email)

class Subscribe(models.Model):
    email = models.CharField(max_length=120)

    def __str__(self):
        return self.email
    
class gallery_photo(models.Model):
    image =models.ImageField(upload_to='gallery/img')

from django.db import models

class FormMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=15)
    optionC = models.CharField(max_length=10)
    message = models.TextField()

    def __str__(self):
        return self.name

from django.db import models

class Comment(models.Model):
    author = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} - {self.created_at}"


class boxform(models.Model):
    ICON_CHOICES = (
        ('icon-project-manangement', 'project Icon'), 
        ('icon-process-development', 'process Icon'),
        ('icon-commitment', 'commitment Icon'),
        ('icon-human-resources', 'Human Icon'),
        ('icon-operation', 'operation Icon'),
        ('icon-business-analysis', 'Business Icon'), 
    
    )
    spanclassname = models.CharField(max_length=200, choices=ICON_CHOICES)
    name =models.CharField(max_length=200)
    title =models.CharField(max_length=200)

class EmailMessage(models.Model):
    email=models.EmailField()
    def __str__(self):
        return self.email
    
    
    
class ReceptPost(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog/images/')
    content = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title
    
