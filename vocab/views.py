from django.shortcuts import render
from django.http import HttpResponse
from .models import Word

# Create your views here.

def storewords(request):
    l = []
    tmp = []
    length = len(Word.objects.all())
    length1 = 0
    wrds = []
    alphabets = []
    for i in range(26):
        alphabets.append(chr(i+65))
        select = Word.objects.all().filter(new_word__startswith=chr(i+65))
        length1 = len(select)
        #print(chr(i+65),select,length1)
        if(length1!=0):
            for j in range(length1):
                tmp.append(select[j].new_word)
                tmp.append(select[j].meaning)
                tmp.append(select[j].example)
                #print(tmp)
                l.append(tmp)
                tmp = []
            print(chr(i+65))
            wrds.append([chr(i+65),len(l),l])
            print([chr(i+65),len(l),l])
        l = []
    print(alphabets)
    return render(request,'vocab/vocabulary.html',{'words':wrds,'alphabets':alphabets,'range':range(26)})

def tst(request):
    alphabets = []
    for i in range(26):
        alphabets.append(chr(i+65))
    return render(request,'vocab/check.html',{'range':range(26),'alphabets':alphabets})