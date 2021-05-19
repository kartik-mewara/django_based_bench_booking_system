from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Reservation1(models.Model):                                 #edit here
    
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    class Meta:
            verbose_name='make reservation here'
            verbose_name_plural='make reservation here'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('bench1:event-detail', args=(self.id,))                   #edit here

    @property
    def get_html_url(self):
        url = reverse('bench1:event-detail', args=(self.id,))                      #edit here
        return f'<a href="{url}"> {self.name} </a>'


