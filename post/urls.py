
from django.contrib import admin
from django.urls import path
from . import views
app_name='post'
urlpatterns = [
    path('postlist/',views.Post_list)  ,
    path('postdetail/',views.Post_detail ),
]