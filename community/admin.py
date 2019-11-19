from django.contrib import admin
from .models import Post
from .models import Community

# Register your models here.
admin.site.register(Post)
admin.site.register(Community)