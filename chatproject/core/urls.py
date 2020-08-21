from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    path('<str:room_name>/remove/', views.remove_chat_room, name='remove'),
    # users authentication patterns
    path('users/registration/', views.register, name="register"),
    path('users/login/', auth_views.LoginView.as_view(
        template_name='core/users/login.html'), name='login'),
    path('users/logout/', auth_views.LogoutView.as_view(
        template_name='core/users/logout.html'), name='logout'),
    path('users/profile/', views.profile, name='profile'),
    # end users authentication
]
