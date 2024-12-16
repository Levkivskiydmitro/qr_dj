from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length= 255)
    email = models.CharField(max_length= 255)
    date_of_birth = email = models.CharField(max_length= 255)

    def __repr__(self) -> str:
        return f"id: {self.id}"



from main.settings import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)

    def __repr__(self) -> str:
        return f"id: {self.id}"
