from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import uuid

# Create your models here.
namespace_uuid = uuid.UUID('6ba7b810-9dad-11d1-80b4-00c04fd430c8')

class Topic(models.Model):
    """Instances of Topic model."""
    id = models.URLField(primary_key=True, default=uuid.uuid5(namespace_uuid, "topic"), editable=False)
    name = models.CharField(max_length=100, null=False)
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        """Display name of topic."""
        return self.name
    

class TopicDetail(models.Model):
    """Instances of TopicDetails."""
    id = models.URLField(primary_key=True, default=uuid.uuid5(namespace_uuid, "topicdetail"), editable=False)
    title = models.ForeignKey(Topic, on_delete=models.CASCADE)
    content = models.TextField()
    student = models.CharField(max_length=100, null=False)
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        """Return topic."""
        return self.content[:50]

