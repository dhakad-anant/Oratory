from django.urls import path
from . import views

app_name = 'vocab'

urlpatterns = [
    path('',views.storewords,name='storewords'),
]