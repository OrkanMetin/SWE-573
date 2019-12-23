from django.contrib import admin
from .models import Post, User
from .models import PostTypeObject
from .models import Community


# Register your models here.
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Community)
admin.site.register(PostTypeObject)