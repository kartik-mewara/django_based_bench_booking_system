

from django.contrib import admin
from bench3.models import Reservation3   #, EventMember

# class EventMemberAdmin(admin.ModelAdmin):
#     model = EventMember
#     list_display = ['event', 'user']

admin.site.register(Reservation3)
# admin.site.register(EventMember, EventMemberAdmin)
admin.site.site_header='Book your reservation here'
