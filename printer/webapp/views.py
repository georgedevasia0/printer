from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import os
import json
def index(request):
    clients=['static/img/clients/'+name for name in os.listdir('static/img/clients')]
    f = open ('static/main.json', "r")
    info=json.loads(f.read())
    print(info['phone'])
    return render(request,'index.html',{'clients':clients,'info':info})