from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, register, login
from .views import VideoViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'videos', VideoViewSet)


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('', include(router.urls)),
    path('api/', include(router.urls)),

]
