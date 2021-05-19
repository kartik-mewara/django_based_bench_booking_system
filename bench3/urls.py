from django.urls import path

from . import views

app_name = 'bench3'
urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.CalendarView.as_view(), name='bench3'),
    path('event1/new/', views.create_event, name='event_new'),
    path('event1/edit/<int:pk>/', views.EventEdit.as_view(), name='event_edit'),
    path('event1/<int:event_id>/details/', views.event_details, name='event-detail'),
    # path('add_eventmember/<int:event_id>', views.add_eventmember, name='add_eventmember'),
    # path('event1/<int:pk>/remove', views.EventMemberDeleteView.as_view(), name="remove_event"),
]
