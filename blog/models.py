from django.db import models

# Create your models here.
class Post(models.Model):
    srn=models.BigAutoField(primary_key=True)
    title= models.CharField(max_length=100)
    content=models.TextField()
    author= models.CharField(max_length=20)
    slug= models.CharField(max_length=50,blank=True)
    image=models.ImageField(upload_to='static/blog',blank=True)
    date=models.DateTimeField(blank=True)
    
    def __str__(self):
        return self.title+"-Author-"+self.author

