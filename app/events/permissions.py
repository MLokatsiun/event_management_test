from rest_framework import permissions

class IsOrganizerOrReadOnly(permissions.BasePermission):
    """
    Custom permission class to allow only the event organizer to edit or delete the event.

    Permissions:
    - SAFE_METHODS (GET, HEAD, OPTIONS): Allowed to any user (authenticated or not).
    - Editing methods (POST, PUT, PATCH, DELETE): Allowed only to authenticated users who
      are the organizer of the event instance.

    This ensures that:
    - Anyone can view event details.
    - Only the event's organizer can modify or delete it.
    """

    def has_permission(self, request, view):
        # Allow all users to read-only methods
        if request.method in permissions.SAFE_METHODS:
            return True
        # For modifying requests, user must be authenticated
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Read-only methods are always allowed
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write/delete permissions only for the organizer of the event
        return obj.organizer == request.user


