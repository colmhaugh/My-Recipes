from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True) 
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipe_posts")
    created_on = models.DateTimeField(auto_now_add=True)    
    ingredients = models.TextField()
    instructions = models.TextField()
    excerpt = models.TextField(blank=True)
    image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(User, related_name='recipe_likes', blank=True)
    # course = models.ForeignKey(
    #    Course, on_delete=models.CASCADE)    
    # description = models.TextField()    

    class Meta:
        ordering = ["-created_on"] #Might change to number of likes

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):    
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="comments")
    comment_text = models.TextField(max_length=500)
    user_name = models.CharField(max_length=50)                       
    # user_name = models.ForeignKey(
    #     User, on_delete=models.CASCADE)    
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.comment_text} by {self.user_name}"

#COURSE = ((0, "Starter"), (1, "Main"), (2, "Dessert"))

# class Course(models.Model):
#     title = models.CharField(max_length=200) 
#     slug = models.SlugField(max_length=200, unique=True)

#     def __str__(self):
#         return self.title