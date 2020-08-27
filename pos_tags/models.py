from django.db import models



class PosTag(models.Model):
    tag = models.CharField(max_length=30)
    description = models.TextField()
    analyzer = models.CharField(max_length=30)
    
