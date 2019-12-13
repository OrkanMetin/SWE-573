from django.urls import path
from . import views
from mysite import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('post_list', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('', views.community_list, name='community_list'),
    path('community_list', views.community_list, name='community_list'),
    path('post_list', views.post_list, name='post_list'),
    path('community/<int:pk>/', views.community_detail, name='community_detail'),
    path('community_detail', views.community_detail, name='community_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('<str:community_name>/new-data-type', views.new_data_type, name='new_data_type'),
    path('create-data-type/<str:community_id>', views.create_data_type, name='create_data_type'),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
