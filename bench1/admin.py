

from django.contrib import admin
from bench1.models import Reservation1     #edit here

admin.site.register(Reservation1)           #edit here

admin.site.site_header='Book your reservation here'