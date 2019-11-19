from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Community
# Create your views here.


def community_list(request):
    communities = Community.objects.order_by('name')
    return render(request, 'community/community_list.html', {'communities': communities})


def community_detail(request, pk):
    community = Community.objects.get(pk=pk)
    return render(request, 'community/community_detail.html', {'community': community})
