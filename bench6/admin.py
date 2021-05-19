

from django.contrib import admin
from bench6.models import Reservation6   #, EventMember

# class EventMemberAdmin(admin.ModelAdmin):
#     model = EventMember
#     list_display = ['event', 'user']

admin.site.register(Reservation6)
# admin.site.register(EventMember, EventMemberAdmin)
