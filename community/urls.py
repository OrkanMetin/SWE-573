from django.urls import path
from . import views
from mysite import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('search', views.search_results, name='search_results'),
    path('post_list', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/new/', views.post_new, name='post_new'),

    path('manage_community/<int:pk>', views.manage_community, name='manage_community'),
    path('community_list', views.community_list, name='community_list'),
    path('community_detail/<int:pk>/', views.community_detail, name='community_detail'),

    path('list_my_communities', views.list_my_communities, name='list_my_communities'),
    path('join_my_communities', views.join_my_communities, name='join_my_communities'),
    path('join_unjoin_communitiy/<int:pk>', views.join_unjoin_communitiy, name='join_unjoin_communitiy'),

    path('new_post/<int:pk>', views.new_post, name='new_post'),
    path('new_generic_post_type/<int:pk>', views.new_generic_post_type, name='new_generic_post_type'),
    path('new_data_type_object/<int:pk>/<int:id>', views.new_data_type_object, name='new_data_type_object'),
    # path('create-data-type/<str:community_id>', views.create_data_type, name='create_data_type'),
    path('create_community', views.create_community, name='create_community'),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
