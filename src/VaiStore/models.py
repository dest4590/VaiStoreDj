from django.db import models
from django.conf import settings
from glob import glob
import os

if os.name != 'nt':
    server_path = str(settings.BASE_DIR)[1:]
else:
    server_path = str(settings.BASE_DIR)

if settings.DEBUG:
    print('Server Path: ' + server_path)

def file_path(instance, filename):
    file_extension = '.' + filename.split(".")[-1]

    if isinstance(instance, App):
        appPath = 'VaiStore/static/img/apps/' + instance.app_id
        if not os.path.isdir(appPath):
            os.mkdir(appPath)
            
        return appPath + '/icon' + file_extension
    
    if isinstance(instance, AppScreenShot):
        appPath = 'VaiStore/static/img/apps/' + instance.app.app_id
        if not os.path.isdir(appPath + '/screenshots/'):
            os.mkdir(appPath + '/screenshots/')

        return appPath + '/screenshots/' + 'Screenshot' + str(len(glob(appPath + '/screenshots/*')) + 1) + file_extension

class App(models.Model):
    name = models.CharField(default='App', help_text='Укажите название приложения', max_length=30)
    app_id = models.CharField(default='AppID', help_text='Укажите айди приложения, по типу TheGame', max_length=200)
    app_size = models.CharField(default='30', help_text='Укажите размер приложения', max_length=4)
    author = models.CharField(default='SuperStudio', help_text='Укажите разработчикаю приложения', max_length=50)
    description = models.CharField(default='The Game 2.0', help_text='Укажите описание приложения', max_length=400)
    image = models.ImageField(upload_to = file_path, help_text='Выберите картинку, png')
    link = models.CharField(default='https://example.com/Game.apk', help_text='Ссылка на приложение', max_length=500)

    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('app_id',)

class AppScreenShot(models.Model):
    app = models.ForeignKey(App, on_delete= models.CASCADE, related_name='files')
    file = models.FileField(upload_to = file_path, null = True, blank = True)

    def __str__(self):
        return 'AppScreenshots'
    
class ChangeLog(models.Model):
    version = models.CharField(max_length=4)
    changes = models.TextField()
    release_date = models.DateField()

    def __str__(self):
        return f"Version {self.version}"
