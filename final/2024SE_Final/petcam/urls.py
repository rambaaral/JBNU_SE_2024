from django.urls import path
from . import views

app_name = 'petcam'

urlpatterns = [
    path('', views.index, name='index'),
    path('reset/', views.reset_system, name='reset_system'),
    path('start-recording/', views.start_recording, name='start_recording'),
    path('toggle-motion/', views.toggle_motion_view, name='toggle_motion'),
    path('get-motion-status/', views.get_motion_status_view, name='get_motion_status'),
]
