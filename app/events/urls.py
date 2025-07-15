from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet

router = DefaultRouter()
router.register(r'', EventViewSet, basename='event')

urlpatterns = [
    path('', include(router.urls)),
]

"""
URL routes exposed:

- /api/events/ [GET, POST]: List events or create a new event.
- /api/events/{id}/ [GET, PUT, PATCH, DELETE]: Retrieve, update, or delete specific event.
- /api/events/{id}/register/ [POST]: Register the authenticated user to the event.

This uses DefaultRouter to automatically generate routes.
"""
