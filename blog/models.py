from django.db import models

# Create your models here.
class Post(models.Model):
    srn=models.BigAutoField(primary_key=True)
    title= models.CharField(max_length=30)
    content=models.TextField()
    author= models.CharField(max_length=10)
    date=models.DateTimeField(blank=True)
    
    def __str__(self):
        return self.title+"-Author-"+self.author
