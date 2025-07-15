from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, status, serializers
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.mail import send_mail
from drf_yasg.utils import swagger_auto_schema
from .models import Event, EventRegistration
from .serializers import EventSerializer, EventRegistrationSerializer
from .permissions import IsOrganizerOrReadOnly


class EmptySerializer(serializers.Serializer):
    """
    A serializer with no fields used for endpoints that don't require any input data.
    Useful for POST requests without request body payload.
    """
    pass


class EventViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Event objects.

    Available endpoints:
    - **List events**:
      `GET /api/events/`
      Returns a list of all events. Supports filtering by `date`, `location`, and `title`.

    - **Retrieve event details**:
      `GET /api/events/{id}/`
      Returns details of a specific event by ID.

    - **Create event**:
      `POST /api/events/`
      Creates a new event. Requires authentication. The `organizer` is automatically set to the current user.

    - **Update event**:
      `PUT /api/events/{id}/` or `PATCH /api/events/{id}/`
      Updates an event. Only the organizer of the event can update it.

    - **Delete event**:
      `DELETE /api/events/{id}/`
      Deletes an event. Only the organizer of the event can delete it.

    - **Register for event**:
      `POST /api/events/{id}/register/`
      Registers the authenticated user for the specified event.
      Request body is empty.
      Returns:
        - `201 Created` if registration is successful.
        - `200 OK` if already registered.

    Permissions:
    - Only authenticated users can create events.
    - Only the organizer can update or delete their own events.
    - Anyone (authenticated or anonymous) can list and retrieve events.
    - Only authenticated users can register for events.

    Filtering:
    - Events can be filtered by:
        - `date`
        - `location`
        - `title`
      Example: `/api/events/?location=Kyiv&date=2025-07-20`
    """

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsOrganizerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date', 'location', 'title']

    def perform_create(self, serializer):
        """
        Assign the requesting user as the organizer of the newly created event.
        """
        serializer.save(organizer=self.request.user)

    @swagger_auto_schema(
        request_body=EmptySerializer,
        responses={
            201: 'registered',
            200: 'already registered'
        }
    )
    @action(
        detail=True,
        methods=['post'],
        serializer_class=EmptySerializer,
        permission_classes=[permissions.IsAuthenticated]
    )
    def register(self, request, pk=None):
        """
        Register the authenticated user for the event specified by pk.

        If the user is successfully registered (first time), send confirmation email.

        Returns JSON with status indicating registration result.
        """
        event = self.get_object()
        registration, created = EventRegistration.objects.get_or_create(
            event=event,
            user=request.user
        )
        if created:
            send_mail(
                subject='Event Registration Confirmation',
                message=f'You registered for "{event.title}".',
                from_email='bosmisa380@gmail.com',
                recipient_list=[request.user.email],
            )
            return Response({'status': 'registered'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'status': 'already registered'}, status=status.HTTP_200_OK)
