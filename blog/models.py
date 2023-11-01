from django.db import models

# Create your models here.


class Post(models.Model):
    #image
    #author
    title=models.CharField(max_length=300)
    content=models.TextField()
    #tag
    #category
    counted_view=models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    publised_date=models.DateTimeField(null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now_add=True)

    class Meta():
        ordering=['-created_date']
    


    def __str__(self):
        return self.title
    


