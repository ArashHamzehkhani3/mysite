from django.db import models
# Create your models here.



class Category(models.Model):
        name=models.CharField(max_length=255)

        def __str__(self):
            return self.name
    



class Post(models.Model):
    image=models.ImageField(upload_to='media/',default='media/default.jpg')
    title=models.CharField(max_length=300)
    content=models.TextField()
    #tag
    category=models.ManyToManyField(Category)
    counted_view=models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    publised_date=models.DateTimeField(null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now_add=True)

    class Meta():
        ordering=['-created_date']
    


    def __str__(self):
        return self.title
    

    

