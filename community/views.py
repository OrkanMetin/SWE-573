from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from .forms import PostForm
from .models import Community, Post, PostType, PostTypeObject


# Create your views here.


def community_list(request):
    community = Community.objects.order_by('name')
    return render(request, 'community/community_list.html', {'community': community})


def community_detail(request, pk):
    community = Community.objects.get(pk=pk)
    posts = Post.objects.get(pk=pk)
    context = {
        "community" : community,
        "posts" : posts
    }
    return render(request, 'community/community_detail.html', context)


# def community_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         community = PostForm(request.POST)
#         if community.is_valid():
#             comment = community.save(commit=False)
#             comment.post = post
#             comment.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         community = PostForm()
#     return render(request, 'community/community_detail.html', {'community': community})


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

# NEW DATA TYPE


def new_data_type(request, community_name):
    community = get_object_or_404(Community, name=community_name)
    context = {
        'community': community,
    }
    return render(request, 'community/new_post_type.html', context)


def create_data_type(request, community_id):
    print(request.POST)
    community = get_object_or_404(Community, pk=community_id)
    if "cancel" in request.POST:
        return HttpResponseRedirect(reverse('vircom:community_detail', args=(community.name,)))
    name = str(request.POST.get('title', "")).strip()
    print(name)
    data_type = PostTypeObject(name=name, community=community, fields={})
    field_list = data_type.fields
    f = {}
    f['fields'] = []
    response = dict(request.POST.lists())
    data_type_list = PostTypeObject.objects.filter(community=community, is_archived=False)
    for dt in data_type_list:
        if dt.name == name and dt.name != data_type.name:
            return render(request, 'vircom/new_data_type.html', {
            'community': community,
            'data_type': data_type,
            'field_list': field_list,
            'error_message': "There is a data type called " + name + " in this community.",
        })
    if data_type.name == "":
        return render(request, 'vircom/new_data_type.html', {
            'community': community,
            'data_type': data_type,
            'field_list': field_list,
            'error_message': "Title field cannot be empty.",
        })
    else:
        data_type.name = name
    if request.POST.get('name') == None:
        return render(request, 'vircom/new_data_type.html', {
            'community': community,
            'data_type': data_type,
            'field_list': field_list,
            'error_message_fields': "You need to add at least one field.",
        })
    for key in range(len(response['name'])):
        if response['name'][key].strip() == "":
            return render(request, 'vircom/new_data_type.html', {
                'community': community,
                'data_type': data_type,
                'field_list': field_list,
                'error_message_fields': "Field Name cannot be empty.",
            })
        else:
            for field in f['fields']:
                if response['name'][key].strip() == field['name']:
                    return render(request, 'vircom/new_data_type.html', {
                        'community': community,
                        'data_type': data_type,
                        'field_list': field_list,
                        'error_message_fields': "You cannot use same field name twice.",
                    })
        field_id = response['fieldId'][key]
        options = []
        field_enumerated = response['enumerated'+field_id][0]
        try:
            multi_choice = response['multiChoice'+field_id][0]
        except KeyError:
            multi_choice = "off"
        if field_enumerated == "Yes":
            options = response['option'+field_id]
        field_name = response['name'][key].strip()
        field_type = response['type'][key]
        field_required = response['required'][key]
        f['fields'].append(
            {
                "name": field_name,
                "field_id": field_id,
                "field_type": field_type,
                "required": field_required,
                "enumerated": field_enumerated,
                "multi_choice": multi_choice,
                "options": options
            }
        )
    data_type.fields = f
    data_type.save()
    return HttpResponseRedirect(reverse('community_detail', args=(community.name,)))
