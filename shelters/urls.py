from django.urls import path
from .views import create_states

urlpatterns = [
    path('create_states/', create_states, name='create_states')
]
