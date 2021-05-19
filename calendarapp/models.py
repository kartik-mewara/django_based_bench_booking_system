from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Event(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
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
        return reverse('calendarapp:event-detail', args=(self.id,))

    @property
    def get_html_url(self):
        url = reverse('calendarapp:event-detail', args=(self.id,))
        return f'<a href="{url}"> {self.name} </a>'

        



# class EventMember(models.Model):
#     event = models.ForeignKey(Event, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     class Meta:
#         unique_together = ['event', 'user']

#     def __str__(self):
#         return str(self.user)