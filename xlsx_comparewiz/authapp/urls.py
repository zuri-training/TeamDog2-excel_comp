from django.urls import path
from .views import register, login, home, logoutUser, about, contact

urlpatterns = [
    path('login/', login, name="login"),
    path('', home, name="home"),
    path('register/', register, name="register"),
    path('logout/', logoutUser, name="logout"),
    path('about', about, name = 'about'),
    path('contact', contact, name = 'contact')
]