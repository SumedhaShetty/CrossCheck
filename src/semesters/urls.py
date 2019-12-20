#from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path, include
from . import views
from semesters import views as semesters_views

app_name = 'semesters'

urlpatterns = [
    #path('',include('CrossCheck.urls')),
    #r'^sems/(?P<id>\d+)/$'
    path('sems/',views.sems, name='sems'),
    path('sems/post_create/',views.post_create, name="post_create"),
    path('sems/post_detail/<int:id>',views.post_detail, name="post_detail"),   
    path('sems/post_list/',views.post_list, name="post_list"),
    path('sems/post_update/',views.post_update, name="post_update"),
    path('sems/post_delete/',views.post_delete, name="post_delete"),
 
]