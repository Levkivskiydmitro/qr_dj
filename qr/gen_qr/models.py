from django.db import models

# Create your models here.
class QR(models.Model):
    url = models.URLField(max_length=200)
    #width = models.IntegerField()
    #height = models.IntegerField() 
    color = models.CharField(max_length=20, default="black")
    #shape = models.CharField()
    img = models.ImageField(upload_to='qr/img', null=True)

    #qr = models.BigIntegerField()


    def __str__(self):
        return f'{self.url}'