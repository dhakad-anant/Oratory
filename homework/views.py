from django.shortcuts import render
from django.http import HttpResponse
from . import forms
import random
from .models import Person
from django.core.mail import send_mail


def index(request):
    return HttpResponse("<h1> now we are starting the app at oratory site yeeeee-----</h1>")


def assignhomework(request):
    
    nametoemail = Person.objects.all()
    newlist = []
    newlist.append('blank')
    for person in nametoemail:
        newlist.append(person.name)
    '''
    indextoname = {}
    count = 1
    for k in nametoemail.keys():
        indextoname[count] = k
        count = count + 1'''
    length = len(newlist)-1

    dict = {}
    visited = [False for i in range(length)]
    print(len(visited))
    flag,current = 0,0
    for i in range(length):
        while(not flag):
            current = random.randint(0,length-1)
            if (not(visited[current])) and current!=i:
                visited[current] = True
                dict[i+1] = current+1
                flag = 1
        flag = 0

    return render(request,'homework/assign.html',{'newlist':newlist,'dict':dict,'range':range(1,15)})
    
    
def sendhomework(request,sender_id,reciever_id):
    sender = Person.objects.get(pk=sender_id)
    reciever = Person.objects.get(pk=reciever_id)
    
    return render(request , 'homework/message.html', {'sender':sender,'reciever':reciever})