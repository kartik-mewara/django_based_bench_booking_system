

from django.contrib import admin
from bench4.models import Reservation4   #, EventMember

# class EventMemberAdmin(admin.ModelAdmin):
#     model = EventMember
#     list_display = ['event', 'user']

admin.site.register(Reservation4)
# admin.site.register(EventMember, EventMemberAdmin)

admin.site.site_header='Book your reservation here'
