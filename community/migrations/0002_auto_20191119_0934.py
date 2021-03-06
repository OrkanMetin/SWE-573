# Generated by Django 2.2.7 on 2019-11-19 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='community',
            old_name='communityPhoto',
            new_name='community_photo',
        ),
        migrations.RenameField(
            model_name='community',
            old_name='communityDesc',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='community',
            old_name='isActive',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='community',
            old_name='communityMembers',
            new_name='members',
        ),
        migrations.RenameField(
            model_name='community',
            old_name='communityName',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='community',
            old_name='communityOwner',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='community',
            old_name='communitySemanticTag',
            new_name='semantic_tag',
        ),
        migrations.RenameField(
            model_name='fieldtype',
            old_name='isNull',
            new_name='is_null',
        ),
        migrations.RenameField(
            model_name='fieldtype',
            old_name='maxLength',
            new_name='max_length',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='postBody',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='postCreator',
            new_name='creator',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='isActive',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='postCreationDate',
            new_name='publish_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='relatedCommunity',
            new_name='related_community',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='relatedPostType',
            new_name='related_post_type',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='postTag',
            new_name='semantic_tag',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='postTitle',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='postdetails',
            old_name='relatedPost',
            new_name='related_post',
        ),
        migrations.RenameField(
            model_name='posttype',
            old_name='postTypeDesc',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='posttype',
            old_name='isActive',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='posttype',
            old_name='postTypeName',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='userMail',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='userName',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='isActive',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='userPassword',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='userSurname',
            new_name='surname',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user',
            new_name='user_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='userPhoto',
            new_name='user_photo',
        ),
        migrations.RemoveField(
            model_name='community',
            name='communityCreationDate',
        ),
        migrations.RemoveField(
            model_name='user',
            name='creationDate',
        ),
    ]
