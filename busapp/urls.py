from django.urls import path,include
from .views import *

urlpatterns = [
    path('project',click_photo_enter, name='project' ),
]