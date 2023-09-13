from django.shortcuts import render, HttpResponse
from .models import App, AppScreenShot, ChangeLog

import random
phrases = ['xdd', 'reload site', 'why?', 'idk', 'please go out', '''
This text is written without any purpose or meaning. It carries no information and has no meaning. Its words simply fit together to create a meaningless sequence of sounds. But perhaps it is in this meaninglessness that its essence lies. We should just enjoy the sound of these words and not look for any meaning in them. Or maybe it's all just part of a larger plan that we don't yet understand. Either way, this text has no value and is not worthwhile
''']



def index(request):
    #return HttpResponse(random.choice(phrases))
    apps = App.objects.all()
    
    appdata = {'apps': apps}

    return render(request, 'index.html', appdata)

def app(request, AppID):
    app = App.objects.get(app_id=AppID)

    appscreenshots = [screenshot if isinstance(screenshot.app, type(app)) else None for screenshot in AppScreenShot.objects.all()]

    return render(request, 'app.html', {'app': app, 'screens': appscreenshots})

def settings(request):
    return render(request, 'settings.html')

def changelogs(request):
    changelogs = ChangeLog.objects.order_by('-id')

    return render(request, 'changelogs.html', {'changelogs': changelogs})