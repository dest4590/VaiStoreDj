from django.contrib import admin
from .models import App, AppScreenShot, ChangeLog

class AppAdmin(admin.ModelAdmin):
    list_display = ('name', 'app_id', 'author')

# Register app
class AppScreenshotAdmin(admin.StackedInline):
    model = AppScreenShot

@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    inlines = [AppScreenshotAdmin]

@admin.register(AppScreenShot)
class CaseFileAdmin(admin.ModelAdmin):
    pass

# Register Changelog
admin.site.register(ChangeLog)