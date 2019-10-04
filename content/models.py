from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser
)


# Create your models here.
class Position(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class Company(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField
    picture = models.ImageField
    location = models.CharField(max_length=255)
    website = models.URLField(max_length=255)
    positions = models.ManyToManyField(Position)
    employer_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"


class BaseUser(AbstractBaseUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    profile_picture = models.ImageField
    e_mail = models.EmailField(max_length=255)
    position = models.ManyToManyField(Position)
    company = models.ManyToManyField(Company)


class Feedback(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField
    author = models.ForeignKey(BaseUser, on_delete=models.CASCADE)
    up_count = models.IntegerField(default=0)
    down_count = models.IntegerField(default=0)
    preview_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title}"


class Vote(models.Model):
    vote_type = models.CharField(max_length=255)
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE)
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}"


class Preview(models.Model):
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE)
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}"


class Form(models.Model):
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"
