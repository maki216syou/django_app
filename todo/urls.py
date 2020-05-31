# -*- coding: utf-8 -*-
from django.urls import path
from.import views
from django.urls import include,path

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<list_id>', views.delete, name="delete"),
    path('complete/<list_id>', views.complete, name="complete"),
    path('todo/', include('todo.urls')),
]
