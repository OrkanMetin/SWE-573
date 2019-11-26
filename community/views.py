from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Community, Post


# Create your views here.


def community_list(request):
    community = Community.objects.order_by('name')
    return render(request, 'community/community_list.html', {'community': community})


def community_detail(request, pk):
    community = Community.objects.get(pk=pk)
    return render(request, 'community/community_detail.html', {'community': community})


def post_list(request):
    posts = Post.objects.order_by('title')
    return render(request, 'community/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'community/post_detail.html', {'post': post})
