from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.home,name="home"),
    path('register/',views.Register,name="Register"),
    path('',views.login_view,name="Login"),
    path('logout/',views.logout_view,name="Logout"),
    path('delete/<int:id>/',views.delete_task,name="delete_task"),
    path('complete/<int:id>/', views.complete_task, name='complete_task'),
]
