from django.urls import path
# from .views import generate_kayak_url_view
from .views import checkout_user
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Travel LLM API",
        default_version='v1',
        description="This API takes user to Checkout page of booking site",
        terms_of_service="https://softservedweb.com/",
        contact=openapi.Contact(email="softservedweb@gmail.com"),
        license=openapi.License(name="SSW License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    # path('hotel_url/', generate_kayak_url_view, name='hotel_url'),  # Use path for function-based views
    path('checkout/', checkout_user, name='my-page'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
