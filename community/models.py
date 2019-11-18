from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import JSONField


class User(models.Model):
    """
    Model whose primary purpose is to display user's profile data.
    """
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user')
    userName = models.CharField(max_length=50, null=True, help_text='Enter your name')
    userSurname = models.CharField(max_length=50, null=True, help_text='Enter your surname')
    userMail = models.EmailField()
    userPassword = models.CharField(max_length=50, null=True, help_text='Enter your password')
    creationDate = models.DateTimeField(default=timezone.now)
    userPhoto = models.ImageField(upload_to='users', blank=True)
    isActive = models.BooleanField(null=True)

    def __str__(self):
        return self.user


class Community(models.Model):
    """
    Model whose primary purpose is to display Community's data.
    """
    communityName = models.CharField(max_length=100, null=True, help_text='Enter community name')
    communityDesc = models.CharField(max_length=200, null=True, help_text='Enter community description')
    communitySemanticTag = models.CharField(max_length=100, null=True, help_text='Enter related semantic tag')
    communityPhoto = models.ImageField(upload_to='communities')
    communityOwner = models.ForeignKey(User, related_name='owners', on_delete=models.SET_NULL, null=True)
    communityMembers = models.ManyToManyField(User, related_name='members', help_text='Community members')
    communityCreationDate = models.DateTimeField(default=timezone.now)
    isActive = models.BooleanField(null=True)

    def __str__(self):
        return self.communityName


class FieldType(models.Model):
    name = models.CharField(max_length=100, null=True, help_text='Enter data type name')
    # CharField eg: Geolocation
    maxLength = models.CharField(max_length=100, null=True, help_text='Maxlength')
    # eg: maxlength=100
    isNull = models.CharField(max_length=100, null=True, help_text='Can be null?')

    # eg: maxlength=100

    def __str__(self):
        return self.name


class PostType(models.Model):
    postTypeName = models.CharField(max_length=100, null=True, help_text='Enter post type name')
    postTypeDesc = models.CharField(max_length=1200, null=True, help_text='Enter post type description')
    isActive = models.BooleanField(null=True)

    def __str__(self):
        return self.postTypeName


class Post(models.Model):
    relatedCommunity = models.ForeignKey(Community, on_delete=models.SET_NULL, null=True)
    relatedPostType = models.ForeignKey(PostType, on_delete=models.SET_NULL, null=True)
    postTitle = models.CharField(max_length=100, null=True, help_text='Enter title of post as text')
    postBody = models.CharField(max_length=200, null=True, help_text='Enter body of post as text')
    postTag = models.CharField(max_length=100, null=True, help_text='Tag comes from related community tag')
    isActive = models.BooleanField(null=True)
    postCreator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    postCreationDate = models.DateTimeField(null=True)

    def __str__(self):
        return self.postTitle


class PostDetails(models.Model):
    relatedPost = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    data = JSONField()

    # JSON field will have all the data fields defined by Community Owner.

    def __str__(self):
        return self.data
