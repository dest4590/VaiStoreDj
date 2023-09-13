from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
import VaiStore.views

urlpatterns = [
    path('', VaiStore.views.index),
    path('app/<str:AppID>', VaiStore.views.app),
    path('settings/', VaiStore.views.settings),
    path('changelogs/', VaiStore.views.changelogs),
    path('admin/', admin.site.urls)] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
