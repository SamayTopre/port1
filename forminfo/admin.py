from django.contrib import admin

from forminfo .models import forminfo

class forminfoadmin(admin.ModelAdmin):
    list_display=('name','mail','phone')

admin.site.register(forminfo,forminfoadmin)
