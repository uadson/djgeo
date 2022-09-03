from django.urls import path

from core.views import get_index


app_name = 'core'

urlpatterns = [
    path('', get_index, name='index'),
]
