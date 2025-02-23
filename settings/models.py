from django.db import models
from datetime import date

def default_expiry_date():
    return date.today().replace(year=date.today().year + 1)

class Card(models.Model):
    num = models.IntegerField()
    end_date = models.DateField(default=default_expiry_date)
    cvv = models.CharField(max_length=4)

    def __repr__(self):
        return f'{self.num}'