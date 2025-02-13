from django.db import models
from django.utils import timezone

class DJPost(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    likes_count = models.IntegerField(default=0)
    author_id = models.IntegerField(null=True, blank=True)
    is_published = models.BooleanField(default=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    