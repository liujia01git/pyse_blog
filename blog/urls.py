from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    #/blog
    path('<int:post_id>/show', views.show,name='show'),
    #/blog/1/show    /blog/2/show
]