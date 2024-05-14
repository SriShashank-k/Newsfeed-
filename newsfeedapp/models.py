from django.db import models
from django.contrib.auth.models import User

class Headline(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    url = models.URLField()
    source_name = models.CharField(max_length=255)
    published_at = models.DateTimeField()
    category = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    language = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    headline = models.ForeignKey(Headline, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.headline.title} by {self.user.username}"
    
