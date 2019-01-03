from django.db import models


class Hello(models.Model):

    title = models.CharField(max_length=20)
    content = models.TextField()
    user = models.CharField(max_length=30)

    def __str__(self):
        return self.title
