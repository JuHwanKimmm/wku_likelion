from django.db import models
# Create your models here.


class World(models.Model):

    title = models.CharField(max_length=20)
    content = models.TextField()
    user = models.CharField(max_length=30)

    def __str__(self):
        return self.title
