from django.urls import path
from .views import home_view,create_job_view

urlpatterns = [
    path('',home_view,name='home'),
    path('post-job/', create_job_view, name='post_job'),
]
