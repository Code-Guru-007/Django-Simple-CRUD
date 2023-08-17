from django.db import models

# Create your models here.

class User(models.Model):
    id = models.CharField(max_length=24, primary_key=True)
    avatar = models.ImageField(upload_to='avatars/')
    bio = models.CharField(max_length=100)
    can_hire = models.BooleanField(default=False)
    country = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)  # Store hashed password
    first_name = models.CharField(max_length=50)
    is_public = models.BooleanField(default=True)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=20)
    state = models.CharField(max_length=50)
    timezone = models.CharField(max_length=20)

    def __str__(self):
        return self.username
