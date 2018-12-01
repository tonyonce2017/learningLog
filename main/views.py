from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    """主页"""
    return render(request, 'main/index.html')


@login_required
def topics(request):
    """显示所有主题"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'main/topics.html', context)


@login_required
def topic(request, topic_id):
    """显示特定主题的所有条目"""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = { 'topic': topic, 'entries': entries}
    return render(request, 'main/topic.html', context)


@login_required()
def new_topic(request):
    """添加新的主题"""
    if request.method != 'POST':
        # 未提交数据, 创建一个新的表单
        form = TopicForm()
    else:
        # POST提交数据, 对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('main:topics'))

    context = {'form': form}
    return render(request, 'main/new_form.html', context)


@login_required()
def new_entry(request, topic_id):
    """添加新的条目"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # 创建一个新的空表单
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('main:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'main/new_entry.html', context)


@login_required()
def edit_entry(request, entry_id):
    """编辑现有条目"""
    entry = Entry.objects.get(id= entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:topic', args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'main/edit_entry.html', context)


