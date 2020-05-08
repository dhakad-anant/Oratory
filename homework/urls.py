from django.urls import path
from . import views

urlpatterns = [
    #path('index/',views.index,name='homeworkIndex'),
    path('',views.assignhomework,name='assignhomework'),
    path('<int:sender_id>/<int:reciever_id>/',views.sendhomework,name='sendhomework')
]