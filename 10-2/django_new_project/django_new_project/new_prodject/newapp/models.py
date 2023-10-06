from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Authors(models.Model):
    fullname =  models.CharField()
    born_date =  models.CharField()
    born_location =  models.CharField()
    description =  models.TextField()

class Quotes(models.Model):
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Authors,  on_delete=models.CASCADE, default=None, null=True)  
    quotes =  models.CharField()


    


