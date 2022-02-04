from datetime import datetime
from django.http import  HttpResponseRedirect
from django.shortcuts import render
from . import models


def index(request):
    message = None
    message_text = message_time = message_author = ""
    if request.method == 'POST': 
        message_text = request.POST.get('message', "")
        message_author = request.POST.get('username', "Анонім")
        message_time = datetime.now()

        message = models.Message.objects.create(
            text = message_text,
            time = message_time,
            author = message_author,
        )

        message.save()
        return HttpResponseRedirect('/')
    
    message_log = models.Message.objects.all()[:4:-1]

    return render(request, 'index.html', context={'message_log': message_log})