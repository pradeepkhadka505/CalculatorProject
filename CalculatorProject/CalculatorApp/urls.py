

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('submitquery', views.submit_query, name='submitquery')
]