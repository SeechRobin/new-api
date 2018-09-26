from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    """This class represents the bucketlist model."""
    title = models.CharField(max_length=255, blank=True)
    body = models.TextField()
    blurb = image_url = author = models.CharField(max_length=255, blank=True)
    image_url = author = models.CharField(max_length=255, blank=True)
    author = models.CharField(max_length=255, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.title)

class Comments(models.Model):
    news = models.ForeignKey(News, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
