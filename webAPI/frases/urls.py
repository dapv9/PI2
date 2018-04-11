from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from frases import views

# Create a router and registrer our viewsets with it.

router = DefaultRouter()
router.register(r'frases', views.FraseViewSet)
router.register(r'users', views.UserViewSet)




# The API URLs are now determined automatically by the router

urlpatterns = [
    url(r'^', include(router.urls))
]
