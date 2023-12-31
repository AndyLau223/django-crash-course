from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, 'Draft'), (1, 'Publish'))
# Create your models here.


# Create a table called Post in DB
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)
    # if user is deleted from User table, then its blog will be deleted as well.
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title