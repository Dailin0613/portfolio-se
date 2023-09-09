import uuid
from django.db import models
from django.urls import reverse


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, serialize=False, auto_created=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, serialize=False, auto_created=True)
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    content = models.TextField()
    category = models.ManyToManyField(Category, related_name='blog_category')
    created_at = models.DateTimeField(auto_created=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_description(self):
        return self.content[:500]

    def get_content(self):
        return self.content[:4000]

    def get_absolute_url(self):
        return reverse('blog-detail', args=[self.id])
    
    def get_image_absolute_url(self):
        return f'http://127.0.0.1:8000/media/blog/{self.image}'

    class Meta:
        ordering = ['-update_at']
