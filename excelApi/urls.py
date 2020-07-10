from django.urls import path
from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

schema_view = get_schema_view(
   openapi.Info(
      title="EXCEL API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.hng.com/policies/terms/",
      contact=openapi.Contact(email="HNG"),
      license=openapi.License(name=""),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

#TEST WITH '/Swagger'
urlpatterns = [
    path('home', views.index, name='index'),
    path('', views.budget, name='budget'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]
