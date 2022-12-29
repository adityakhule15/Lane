from django.db import models

class count(models.Model):

    pk1=models.CharField(max_length=100)
    like = models.CharField(max_length=100)
    dislike = models.CharField(max_length=12)    
    
    class Meta:
        db_table = "count"
