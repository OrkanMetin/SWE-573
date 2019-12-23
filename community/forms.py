from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

from .models import Post, Community, PostTypeObject


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class PostTypeObjectForm(forms.ModelForm):

    class Meta:
        model = PostTypeObject
        fields = ('name', 'description')


class GenericPostTypeObjectForm(forms.ModelForm):

    class Meta:
        model = PostTypeObject
        fields = ('name', 'description')
        # fields = ('name', 'description','fields')
        # widgets = {
        #     'fields' : forms.
        # }


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'body','is_active')
        # fields = ('title', 'body','slug','semantic_tag','is_active','publish_date','community','post_type','owner')


class CommunityForm(forms.ModelForm):

    class Meta:
        model = Community
        fields = ('name', 'description','community_photo')
