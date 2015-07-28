from django.contrib import admin

from bangbox.models import Bangbox_user, event

# Register your models here.

admin.site.register(Bangbox_user)
admin.site.register(event)
