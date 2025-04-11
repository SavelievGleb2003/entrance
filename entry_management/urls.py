from tkinter.font import names

from django.urls import path


from . import views


urlpatterns = [
    path('', views.list_entrances, name='list_entrances')
]