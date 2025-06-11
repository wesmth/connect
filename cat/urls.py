from . import views
from django.urls import path
urlpatterns = [
    path('',views.random_cat,name='cat')
]
