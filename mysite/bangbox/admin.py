from django.contrib import admin

from bangbox.models import user, event, category, event_date, event_time

# Register your models here.

admin.site.register(user)
admin.site.register(event)
admin.site.register(category)
admin.site.register(event_date)
admin.site.register(event_time)
