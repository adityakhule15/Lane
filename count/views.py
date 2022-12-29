import json
from django.shortcuts import render, redirect
from django.http import HttpResponse

from count.serializers import EntrySerializer
from .models import count
from django.views.decorators.csrf import csrf_exempt 
# Create your views here.

@csrf_exempt
def home(request):
    Entry1=count.objects.all()
    serializer = EntrySerializer(Entry1, many = True)
    abc1 = json.dumps(serializer.data)
    abc = json.loads(abc1)
    print(abc)
    return render(request, 'index.html', {'count':abc})
    

@csrf_exempt
def like(request):
    Entry1=count.objects.all()
    serializer = EntrySerializer(Entry1, many = True)
    abc1 = json.dumps(serializer.data)
    abc = json.loads(abc1)
    c=0
    for p in abc:
        if p['like']:
            c=int(p['like'])+1
    print(c)
    count.objects.filter(pk1='1').update(like=c)
    
    return redirect('http://127.0.0.1:8000/home/')

@csrf_exempt
def dslike(request):
    Entry1=count.objects.all()
    serializer = EntrySerializer(Entry1, many = True)
    abc1 = json.dumps(serializer.data)
    abc = json.loads(abc1)
    c=0
    for p in abc:
        if p['dislike']:
            c=int(p['dislike'])+1
    print(c)
    count.objects.filter(pk1='1').update(dislike=c)
    
    return redirect('http://127.0.0.1:8000/home/')
