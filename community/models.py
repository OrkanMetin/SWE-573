from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import JSONField, ArrayField
from django.db import models
from django.utils import timezone


class User(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    joined_communities = ArrayField(models.IntegerField(), blank=True, null=True)

    def __str__(self):
        return self.user.username


class Community(models.Model):
    """
    Model whose primary purpose is to display Community's data.
    """
    name = models.CharField(max_length=100, null=True, help_text='Enter Community Name')
    description = models.CharField(max_length=200, null=True, help_text='Enter Community Description')
    community_photo = models.ImageField(upload_to='Communities')
    published_date = models.DateTimeField(null=True)
    is_active = models.BooleanField(null=True)
    owner = models.ForeignKey(get_user_model(), related_name='Owners', on_delete=models.PROTECT, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class PostTypeObject(models.Model):
    name = models.CharField(max_length=200, help_text='Enter Post Name')
    description = models.CharField(max_length=200, help_text='Enter Post Description')
    community = models.ForeignKey(Community, on_delete=models.PROTECT)
    fields = JSONField()
    publish_date = models.DateTimeField(null=True)
    is_archived = models.BooleanField(default=False)
    is_generic = models.BooleanField(default=False)
    owner = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, null=True)


class Post(models.Model):
    title = models.CharField(max_length=100, null=True, help_text='Enter Title of Post As Text')
    body = models.CharField(max_length=200, null=True, help_text='Enter Body of Post As Text')
    slug = models.SlugField(max_length=100, null=True)
    semantic_tag = JSONField()
    # semantic_tag = models.CharField(max_length=100, null=True, help_text='Tag Comes From Related Community Tag')
    is_active = models.BooleanField(null=True)
    publish_date = models.DateTimeField(null=True)
    community = models.ForeignKey(Community, on_delete=models.PROTECT)
    post_type = models.ForeignKey(PostTypeObject, on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()