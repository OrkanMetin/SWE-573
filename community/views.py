from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from .forms import PostForm
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


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.creator = request.user
            post.publish_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'community/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.publish_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'community/post_edit.html', {'form': form})
