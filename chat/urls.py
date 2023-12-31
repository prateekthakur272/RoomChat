from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('<str:room>/', views.get_room, name='get room'),
    path('checkroom', views.check_room, name='check room'),
    path('send', views.send, name='send'),
    path('getmessages/<str:room>/', views.get_messages, name='get messages'),
]
