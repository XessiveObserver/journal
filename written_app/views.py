from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Topic, TopicDetail
from .forms import TopicForm, TopicDetailForm

# Create your views here.
def index(request):
    app = "Journal"
    context = {"app": app}
    return render(request, "written_app/index.html", context)
@login_required
def topics(request):
    """Return all topics"""
    topics = Topic.objects.filter(owner=request.user).order_by("date_added")
    context = {
        "topics": topics
    }
    return render(request, "written_app/topics.html", context)

@login_required
def topic(request, topic_id, slug):
    """Return a topic."""
    topic = Topic.objects.get(id=topic_id, slug=slug)
    # Make sure topic belongs to particular user
    if topic.owner != request.user:
        raise Http404
    # Select topic details of a topic
    topic_details = topic.topicdetail_set.order_by("-date_added")

    context = {
        "topic": topic,
        "topic_details": topic_details
    }
    return render(request, "written_app/topic.html", context)

@login_required
def add_topic(request):
    """Create topic."""
    if request.method != "POST":
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            data = Topic(
                name = cd["name"]
            )            
            data.owner = request.user
            data.save()
            return redirect("written_app:topics")
    
    context = {
        "form": form
    }
    return render(request, "written_app/add_topic.html", context)

@login_required
def edit_topic(request, topic_id, slug):
    """Edit topic."""
    topic = get_object_or_404(Topic, id=topic_id, slug=slug)
    if topic.owner != request.user:
        raise Http404

    if request.method != "POST":
        form = TopicForm(initial={
            "name": topic.name
        })
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            topic.name = form.cleaned_data['name']
            topic.save()
            return redirect("written_app:topic", topic_id=topic.id, slug=topic.slug)
    
    context = {
        "form": form,
        "topic": topic
    }
    return render(request, "written_app/edit_topic.html", context)

@login_required
def delete_topic(request, topic_id, slug):
    """Delete post."""
    topic = get_object_or_404(Topic, id=topic_id, slug=slug)
    if request.method == "POST":
        topic.delete()
        return redirect("written_app:topics")
    
    context = {
        "topic": topic
    }
    return render(request, "written_app/delete_topic.html", context)

@login_required
def add_topic_detail(request, topic_id, slug):
    """Adding new topic detail."""
    topic = get_object_or_404(Topic, id=topic_id, slug=slug)
    if request.method != "POST":
        form = TopicDetailForm()
    else:
        form = TopicDetailForm(request.POST)
        if form.is_valid():
            detail = form.save(commit=False)
            detail.topic = topic
            detail.save()
            return redirect("written_app:topic", topic_id=topic_id, slug=slug)
    
    context = {
        "form": form,
        "topic" : topic
    }

    return render(request, "written_app/add_topic_detail.html", context)

@login_required
def edit_topic_detail(request, topic_detail_id, slug):
    """Edit a topic detail."""
    topic_detail = get_object_or_404(TopicDetail, id=topic_detail_id, slug=slug)
    topic = topic_detail.title

    if request.method != "POST":
        form = TopicDetailForm(instance=topic_detail)
    else:
        form = TopicDetailForm(request.POST, instance=topic_detail)
        if form.is_valid():
            form.save()
            return redirect("written_app:topic", topic_id=topic.id, slug=topic.slug)
        
    context = {
        "topic_detail": topic_detail,
        "topic": topic,
        "form": form
    }
    return render(request, "written_app/edit_topic_detail.html", context)

@login_required
def delete_topic_detail(request, topic_detail_id, slug):
    """Delete topic detail."""
    delete_topic_detail = get_object_or_404(TopicDetail, id=topic_detail_id, slug=slug)
    topic = delete_topic_detail.title
    if request.method == "POST":
        delete_topic_detail.delete()
        return redirect("written_app:topic", topic_id=topic.id, slug=topic.slug)
    
    context = {
        "delete_topic_detail": delete_topic_detail
    }
    return render(request, "written_app/delete_topic_detail.html", context)