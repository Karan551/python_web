from django.db import models


# Create your models here.
class Post(models.Model):
    serial_number = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.title + " by " + self.author
