from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import login, authenticate
from datetime import datetime

from .forms import PostForm, CommunityForm, SignUpForm
from .models import Community, Post, PostTypeObject, User

import json

def signup(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            user = User(user=user, joined_communities=[])
            user.save()
            return redirect('home')
    else:
        form = SignUpForm()
    if not request.user.is_authenticated:
        return render(request, 'community/signup.html', {'form': form})
    else:
        return redirect('home')

def home(request):
    community = Community.objects.order_by('name')
    joined_community = ""
    if request.user.is_authenticated:
        joined_community = get_object_or_404(User, user=request.user).joined_communities
    context = {
        "navigation": "home",
        "community": community,
        "joined_community": joined_community,
        "is_authenticated": request.user.is_authenticated
    }
    return render(request, 'community/community_list.html', context)

def about(request):
    context = {
        "navigation" : "about",
        "is_authenticated": request.user.is_authenticated
    }
    return render(request, 'community/about.html', context)

def contact(request):
    context = {
        "navigation" : "contact",
        "is_authenticated": request.user.is_authenticated
    }
    return render(request, 'community/contact.html', context)


def search_results(request):
    community = Community.objects.order_by('name')
    search_text = request.POST['search']
    community = community.filter(name__icontains=search_text)
    joined_community = ""
    if request.user.is_authenticated:
        joined_community = get_object_or_404(User, user=request.user).joined_communities
    context = {
        "navigation": "search_results",
        "search_text" : search_text,
        "community" : community,
        "joined_community" : joined_community,
        "is_authenticated": request.user.is_authenticated
    }
    return render(request, 'community/community_list.html', context)

@login_required
def list_my_communities(request):
    community = Community.objects.order_by("name").filter(owner_id=request.user.id)
    joined_community = get_object_or_404(User, user=request.user).joined_communities
    context = {
        "navigation" : "list_my_communities",
        "community" : community,
        "joined_community" : joined_community,
        "is_authenticated": request.user.is_authenticated
    }
    return render(request, 'community/community_list.html', context)

@login_required
def join_my_communities(request):
    community = Community.objects.filter(pk__in=get_object_or_404(User, user=request.user).joined_communities)
    joined_community = get_object_or_404(User, user=request.user).joined_communities
    context = {
        "navigation" : "join_my_communities",
        "community" : community,
        "joined_community" : joined_community,
        "is_authenticated": request.user.is_authenticated
    }
    return render(request, 'community/community_list.html', context)

@login_required
def join_unjoin_communitiy(request,pk):
    user = get_object_or_404(User, user=request.user)
    if pk not in user.joined_communities:
        user.joined_communities.append(pk)
    else:
        user.joined_communities.remove(pk)
    user.save()
    return HttpResponse("")

def community_list(request):
    community = Community.objects.order_by('name')
    joined_community = get_object_or_404(User, user=request.user).joined_communities
    context = {
        "navigation" : "community_list",
        "community" : community,
        "joined_community" : joined_community,
        "is_authenticated": request.user.is_authenticated
    }
    return render(request, 'community/community_list.html', context)

@login_required
def community_detail(request, pk):
    community = Community.objects.get(pk=pk)
    posts = Post.objects.filter(community_id=pk).order_by("-pk")
    post_type_object = PostTypeObject.objects.filter(community_id=pk)

    context = {
        "navigation": "community_detail",
        "community" : community,
        "posts" : posts,
        "post_type_object" : post_type_object,
        "is_authenticated": request.user.is_authenticated
    }
    return render(request, 'community/community_detail.html', context)

@login_required
def manage_community(request, pk):
    community = get_object_or_404(Community, pk=pk)
    community_obj = Community.objects.get(pk=pk)

    if request.method == "POST":
        if request.FILES:
            if not community.community_photo.name == "Communities/" + datetime.now().strftime("%d.%m.%Y").__str__() + "-" + request.FILES['community_photo'].name:
                file = request.FILES['community_photo']
                file_name = datetime.now().strftime("%d.%m.%Y").__str__() + "-" + file.name
                fs = FileSystemStorage()
                fs.save(file_name, file)
                community.community_photo = "Communities/" + file_name
        form = CommunityForm(request.POST, instance=community)

        if form.is_valid():
            post = form.save(commit=False)
            post.publish_date = timezone.now()
            post.save()
            return redirect('community_detail', pk=post.pk)
    else:
        form = CommunityForm(instance=community)

    context = {
        "navigation": "manage_community",
        "form": form,
        "community": community_obj,
        "is_authenticated": request.user.is_authenticated
    }
    return render(request, 'community/manage_community.html', context)

@login_required
def new_post(request, pk):
    from django.contrib.auth.models import User
    community = get_object_or_404(Community, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.publish_date = timezone.now()
            post.community = community
            parsed_json = []
            for data in request.POST.getlist('wikidata-tag'):
                parsed_json.append(json.loads(data.replace("\\\'", "\"")))
            post.semantic_tag = parsed_json
            # post.post_type = PostTypeObject(name=)
            post.owner = request.user
            post.save()
            return redirect('community_detail', pk=community.pk)
    else:
        form = PostForm()

    context = {
        "navigation": "new_data_type",
        "form": form,
        # "post_type_object": post_type_object,
        "is_authenticated": request.user.is_authenticated
    }
    return render(request, 'community/new_post.html', context)


def new_generic_post_type(request, pk):
    community = get_object_or_404(Community, pk=pk)
    if request.method == "POST":
        name = str(request.POST.get('title', "")).strip()
        post_type = PostTypeObject(name=name, community=community, fields={})
        f = {}
        f['fields'] = []
        response = dict(request.POST.lists())
        for key in range(len(response['title'])):
            field_id = response['fieldId'][key]
            options = []
            try:
                multi_choice = response['multiChoice' + field_id][0]
            except KeyError:
                multi_choice = "off"

            field_name = response['title'][key].strip()
            field_type = response['type'][key]
            field_required = response['required'][key]
            f['fields'].append(
                {
                    "title": field_name,
                    "field_id": field_id,
                    "field_type": field_type,
                    "required": field_required,
                    "multi_choice": multi_choice,
                    "options": options
                }
            )

        post_type.fields = f
        post_type.publish_date = timezone.now()
        post_type.is_generic = True
        post_type.is_archived = False
        post_type.user = request.user
        post_type.save()

        data_type_list = Post.objects.filter(community=community).order_by('pk')
        data_type_object_list = PostTypeObject.objects.filter(community=community).order_by('-publish_date')
        context = {
            'community': community,
            'data_type_list': data_type_list,
            'data_type_object_list': data_type_object_list,
        }

        user = get_object_or_404(User, user=request.user)
        context["user"] = user
        if user.joined_communities:
            if community.pk in user.joined_communities:
                context["joined"] = True
        return render(request, 'community/new_generic_post.html', context)

    context = {
        "navigation": "new_generic_post_type",
        # "form": form,
        # "post_type_object": post_type_object,
        "is_authenticated": request.user.is_authenticated
    }
    return render(request, 'community/new_generic_post_type.html', context)


def new_data_type_object(request, pk, id):
    community = get_object_or_404(Community, pk=pk)
    data_type_list = Post.objects.filter(community=community).order_by('pk')
    data_type_object_list = PostTypeObject.objects.filter(community=community).order_by('-publish_date')
    data_type = get_object_or_404(PostTypeObject, pk=id, community=community)
    context = {
        'community': community,
        'data_type_list':  data_type_list,
        'data_type_object_list': data_type_object_list,
    }
    if request.user.is_authenticated:
        user = get_object_or_404(User, user=request.user)
        context["user"] = user
        if community.pk not in user.joined_communities:
            return render(request, 'community/community_list.html', context)
    fields = data_type.fields
    context = {
        'user': user,
        'community': community,
        'data_type': data_type,
        'fields': fields
    }
    return render(request, 'community/new_generic_post.html', context)



def create_community(request):
    if request.method == 'POST':

        name = str(request.POST.get('name', "")).strip()
        description = str(request.POST.get('description', "")).strip()

        community = Community(name=name, description=description, published_date=timezone.now(),community_photo="Communities/" + request.FILES['community_photo'].name, is_active=True,owner=request.user)

        if request.method == "POST":
            if request.FILES:
                if not community.community_photo.name == "Communities/" + datetime.now().strftime("%d.%m.%Y").__str__() + "-" + request.FILES['community_photo'].name:
                    file = request.FILES['community_photo']
                    file_name = datetime.now().strftime("%d.%m.%Y").__str__() + "-" + file.name
                    fs = FileSystemStorage()
                    fs.save(file_name, file)
                    community.community_photo = "Communities/" + file_name
            form = CommunityForm(request.POST, instance=community)
            if form.is_valid():
                post = form.save(commit=False)
                post.publish_date = timezone.now()
                post.save()
                return redirect('community_detail', pk=post.pk)
        else:
            form = CommunityForm(instance=community)
        community.save()
        return redirect(home)


    else:
        form = CommunityForm()
        context = {
            "navigation": "create_community",
            "form": form,
            "is_authenticated": request.user.is_authenticated
        }
        return render(request, 'community/create_community.html', context)









@login_required
def post_list(request):
    posts = Post.objects.order_by('title')
    context = {
        "navigation": "post_list",
        "posts" : posts,
        "is_authenticated": request.user.is_authenticated
    }
    return render(request, 'community/post_list.html', context)

@login_required
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        "navigation": "post_detail",
        "post" : post,
        "is_authenticated": request.user.is_authenticated
    }
    return render(request, 'community/post_detail.html', context)

@login_required
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

    context = {
        "navigation": "post_new",
        "form" : form,
        "is_authenticated": request.user.is_authenticated
    }
    return render(request, 'community/post_edit.html', context)

@login_required
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

    context = {
        "navigation": "post_edit",
        "form" : form,
        "is_authenticated": request.user.is_authenticated
    }
    return render(request, 'community/post_edit.html', context)
