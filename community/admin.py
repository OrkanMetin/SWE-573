from django.contrib import admin
from .models import Post
from .models import PostType
from .models import FieldType
from .models import PostDetails
from .models import Community
from .models import User


# Register your models here.
admin.site.register(Post)
admin.site.register(Community)
admin.site.register(User)
admin.site.register(PostType)
admin.site.register(FieldType)
admin.site.register(PostDetails)
