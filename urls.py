from django.urls import path
from .import views

urlpatterns = [
    path('', views.login_user, name='login'),
    path('signup', views.signup, name='signup'),
    path('home', views.home, name='home'),
    path('create', views.create_post, name='create'),
    path('viewing/<int:pk>/', views.viewing, name='view'),
    path('logout', views.logout_user, name='logout'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]