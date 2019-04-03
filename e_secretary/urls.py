from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('change_avatar/', views.change_avatar, name='change-avatar'),
    path('my_courses/', views.my_courses, name='my_courses'),
    path('course/<int:didaskalia_id>/', views.course, name='course'),
    path('ergasies/<int:didaskalia_id>/', views.ergasies, name='ergasies'),
    path('ergasies/<int:didaskalia_id>/<int:ergasia_id>/',
         views.ergasies, name='ergasia'),
]
