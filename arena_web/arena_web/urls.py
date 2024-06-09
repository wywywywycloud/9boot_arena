from django.urls import path
from .views import arena_view

urlpatterns = [
    path('', arena_view, name='arena_view'),
]
