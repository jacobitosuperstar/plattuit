from django.urls import path
from . import views

urlpatterns = [
    # Landing Page
    path('', views.micro_blog_view, name='micro_blog'),

    # API
    path(
        'api/microblog/',
        views.api_micro_blog_list_view
    ),
    path(
        'api/microblog/<int:microblog_id>/',
        views.api_micro_blog_detail_view
    ),

    # API create blog
    path(
        'api/microblog/create/',
        views.api_micro_blog_create_view
    ),
]
