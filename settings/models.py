from django.db import models
from datetime import date, timedelta

def default_expiry_date():
    return date.today().replace(year=date.today().year + 1)

# Create your models here.
class Card(models.Model):
    num = models.IntegerField()
    end_date = models.DateField(default=default_expiry_date)
    cvv_code = models.CharField(max_length=4)

    def __repr__(self):
        return f'{self.num}'