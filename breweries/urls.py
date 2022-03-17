from django.urls import include, path
from rest_framework import routers
from application import views

router = routers.DefaultRouter()
router.register(r'brewery', views.BreweryViewSet)

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),

]
