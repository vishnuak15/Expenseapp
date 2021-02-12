from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from app.views import UnicornViewSet

router = DefaultRouter() 
router.register('unicorn', UnicornViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('app.urls')),
    # Authentication
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('authentication/', include('users.urls')),
    # API
    path('v1/', include(router.urls)),
]


