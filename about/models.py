from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
"""
This module defines the models for the 'about' app, which includes an About page and a Collaborate Request model.
These models are used to store information about the site and handle collaboration requests.
"""
class About(models.Model):
    title = models.CharField(max_length=200)
    profile_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title

"""
The CollaborateRequest model is used to store information about collaboration requests made by users.
It includes fields for the requester's name, email, message, and a read status to track whether the request has been addressed.
"""
class CollaborateRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"