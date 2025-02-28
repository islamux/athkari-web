from django.db import models

class Athkar(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.title
