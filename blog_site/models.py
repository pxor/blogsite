from django.db import models


class BlogPost(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title
