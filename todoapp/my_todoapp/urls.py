from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('register/',views.Register,name="Register"),
    path('login/',views.login,name="Login"),
    path('logout/',views.logout,name="Logout"),
    path('delete/<int:id>/',views.delete_task,name="Delete")
]
