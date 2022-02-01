from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Course(models.Model):
    title = models.CharField(max_length=200) 
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.title


class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True) 
    slug = models.SlugField(max_length=200, unique=True)
    image = CloudinaryField('image', default='placeholder')
    description = models.TextField()    
    ingredients = models.TextField()
    directions = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created_on"] #Might change to number of likes

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                             related_name="comments")
    user_name = models.ForeignKey(
        User, on_delete=models.CASCADE)    
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"