from django.contrib import admin

# Register your models here.
from .models import Topic, TopicDetail

admin.site.register(Topic)
admin.site.register(TopicDetail)