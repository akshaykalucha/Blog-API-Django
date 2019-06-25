from django.db import models
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    showcase = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    title_image = models.ImageField(upload_to = 'headres/', default = 'https://i.pinimg.com/originals/3e/9b/50/3e9b50f473182f34b86dc00d80ddf843.jpg')


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={"pk": self.pk})