from django.urls import path, include

from . import api_services


urlpatterns = [
    path('/posts/', include([
        path('detail/<str:id>', api_services.detail_post, name='detail_post'),
        path('create', api_services.create_post, name='create_post'),
        path('update/<str:id>', api_services.update_post, name='update_post'),
        path('delete/<str:id>', api_services.delete_post, name='delete_post'),
        path('vote/<str:id>', api_services.vote_for_post, name='vote_for_post'),
    ])),
    path('/comments/', include([
        path('detail/<str:id>', api_services.detail_comment, name='detail_comment'),
        path('create', api_services.create_comment, name='create_comment'),
        path('update/<str:id>', api_services.update_comment, name='update_comment'),
        path('delete/<str:id>', api_services.delete_comment, name='delete_comment'),
    ])),
]
