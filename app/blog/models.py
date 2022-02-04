from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator

# Create your models here.

class CustomUser(AbstractUser):
    """Model for custom user model"""
    pass
class Tag(models.Model):
    """A post tag"""
    caption = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.caption}"

class Author(models.Model):
    """The model for the Author profile"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Post(models.Model):
    """The model for the Post"""
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, null=False, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    excerpt = models.CharField(max_length=500)
    image_name= models.CharField(max_length=100)
    date  = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name="posts", null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.title}"