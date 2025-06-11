from django.urls import path
from . import views

urlpatterns = [
    path('', views.make_question,name='make_question')
]
