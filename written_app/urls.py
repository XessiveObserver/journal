from django.urls import path
from .views import index, topics, topic, add_topic,\
      edit_topic, delete_topic, add_topic_detail, \
        edit_topic_detail, delete_topic_detail

app_name = "written_app"

urlpatterns = [
    path("", index, name="index"),
    path("topics/", topics, name="topics"),
    path("topic/<slug:slug>/<uuid:topic_id>", topic, name="topic"),
    path("add_topic/", add_topic, name="add_topic"),
    path("edit_topic/<slug:slug>/<uuid:topic_id>", edit_topic, name="edit_topic"),
    path("delete_topic/<slug:slug>/<uuid:topic_id>", delete_topic, name="delete_topic"),
    path("add_topic_detail/<slug:slug>/<uuid:topic_id>", add_topic_detail, name="add_topic_detail"),
    path("edit_topic_detail/<slug:slug>/<uuid:topic_detail_id>", edit_topic_detail, name="edit_topic_detail"),
    path("delete_topic_detail/<slug:slug>/<uuid:topic_detail_id>", delete_topic_detail, name="delete_topic_detail"),
]