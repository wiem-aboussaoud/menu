from django.db import models


# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    created = models.CharField(null=True, blank=True, default="testing", max_length=12)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name