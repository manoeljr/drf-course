from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

import backend.views

router = routers.DefaultRouter()
router.register('contacts', backend.views.ContactViewSet, basename='contacts')


urlpatterns = [
    path('api/v1/', include(router.urls)),

    path('admin/', admin.site.urls),
]
