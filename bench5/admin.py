

from django.contrib import admin
from bench5.models import Reservation5   #, EventMember

# class EventMemberAdmin(admin.ModelAdmin):
#     model = EventMember
#     list_display = ['event', 'user']

admin.site.register(Reservation5)
# admin.site.register(EventMember, EventMemberAdmin)
admin.site.site_header='Book your reservation here'
