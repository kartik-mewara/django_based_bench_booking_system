from django.contrib import admin
from django.contrib.auth.models import Group
from calendarapp.models import Event   #, EventMember

# class EventMemberAdmin(admin.ModelAdmin):
#     model = EventMember
#     list_display = ['event', 'user']

admin.site.register(Event)
# admin.site.register(EventMember, EventMemberAdmin)
admin.site.unregister(Group)
admin.site.site_header='Book your reservation here'