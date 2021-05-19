

from django.contrib import admin
from bench2.models import Reservation2   #, EventMember

# class EventMemberAdmin(admin.ModelAdmin):
#     model = EventMember
#     list_display = ['event', 'user']

admin.site.register(Reservation2)
# admin.site.register(EventMember, EventMemberAdmin)
admin.site.site_header='Book your reservation here'
