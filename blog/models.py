from django.db import models
from django.contrib.auth.models import User


STATUS = ((0,"Draft"), (1,"Published"))
# Create your models here.

# Model is a special class of Django to contain fields of data.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)    # unique URL
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    # if the user is deleted from the user database table, the user posts will also be deleted.
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title