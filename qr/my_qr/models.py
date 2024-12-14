from django.db import models

# Create your models here.
class QR(models.Model):
    url = models.URLField(max_length=200)
    #code = models.ImageField()

    def __str__(self):
        return self.url