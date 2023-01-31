from django.shortcuts import render, redirect
from .models import *


def index(request):
    template = 'index.html'
    context = {}
    
  
    return render (request, template, context)






def startgame(request, thread=1):
    thread = request.GET.get('id')
    template = 'startgame.html'
    start = Thread.objects.get(name='intro')
    triggers = Thread.objects.get(id=thread).from_thread.all()
    next_chapter_id = start.from_thread.filter(action='Далее')
    context = { 'start': start, 'triggers': triggers, 'chapter': next_chapter_id}

    return render (request, template, context)
    