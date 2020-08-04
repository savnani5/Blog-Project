from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User   ## User model given to us by django just like the below post model
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    image = models.ImageField(default = 'default.jpg', upload_to = 'post_pics')
    date_posted = models.DateTimeField(default=timezone.now)
    # to create many to one relation between posts and user
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # cascade means if user is deleted delete all the posts

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class RelatedPost(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(default = 'default.jpg', upload_to = 'related_post_pics')

    def __str__(self):
        return self.title


# Subscription Model Independent of User (anyone who provides the email can subscribe)
class Subscription(models.Model):
    email = models.EmailField(max_length = 255)
