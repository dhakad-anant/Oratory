from django.urls import path
from . import views

urlpatterns = [
    path('',views.storewords,name='storewords'),
]