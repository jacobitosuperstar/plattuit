from django.urls import path
from . import views

urlpatterns = [
    # API
    path(
        'api/like/',
        views.api_micro_blog_add_like_view
    ),
    path(
        'api/dislike/',
        views.api_micro_blog_add_dislike_view
    ),
]
