from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

# Schema view for Swagger/OpenAPI documentation generation
schema_view = get_schema_view(
    openapi.Info(
        title="Event Management API",
        default_version='v1',
        description="API for managing events",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Admin panel route
    path('admin/', admin.site.urls),

    # JWT Authentication endpoints
    path('/api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Obtain JWT access and refresh tokens
    path('/api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh access token using refresh token

    # Include routes for user management app
    path('/api/users/', include('users.urls')),

    # Include routes for event management app
    path('/api/events/', include('events.urls')),

    # Swagger UI for API documentation and testing
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

# Serve static files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
