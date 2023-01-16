from rest_framework import routers
from .api import ProjectViewsets
route = routers.DefaultRouter()
route.register('api/persona', ProjectViewsets, 'persona')
urlpatterns = route.urls
