from django import forms
from .models import TopicDetail, Topic

class TopicForm(forms.ModelForm):
    """TopicForm instance."""
    class Meta:
        model = Topic
        fields = ["name"]

class TopicDetailForm(forms.ModelForm):
    """Topic Detail Form instance."""
    class Meta:
        model = TopicDetail
        fields = "__all__"