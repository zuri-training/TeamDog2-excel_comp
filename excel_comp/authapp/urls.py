from django.urls import path
from .views import register, login, home, logoutUser

urlpatterns = [
    path('login/', login, name="login"),
    #path('', home, name="home"),
    path('register/', register, name="register"),
    path('logout/', logoutUser, name="logout")
]