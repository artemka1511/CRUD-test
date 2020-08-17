from django.urls import path

from . import views  # Точка значит, что из текущего пакета. Импортируем содержимое файлы views.py

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
]