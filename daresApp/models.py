from django.db import models

# Create your models here.
class Votes(models.Model):
    """
    Model to store votes for a specific user and their choice.
    """
    image_id= models.AutoField(primary_key=True)
    image_file=models.ImageField()
    category=models.CharField(max_length=100)
    votes= models.IntegerField(default=0)

    def __str__(self):
        return  f"Image ID: {self.image_id}, Image:{self.image_file} ,Category: {self.category}, Votes: {self.votes}"