from django.urls import include, path
from rest_framework import routers
from . import views



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('apirest/spot/', views.SpotViewSet.as_view()),
    path('apirest/spot/<int:pk>/', views.SpotViewSet.as_view()),

]