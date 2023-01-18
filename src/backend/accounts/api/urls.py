from django.urls import path, include
from .views import (LogoutView, LoginViewSet, ProfileViewSet,
                    CreateProfileViewSet, UpdatePasswordViewSet, UpdateLanguage, userExists)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('profile', ProfileViewSet, basename='users')
router.register('register', CreateProfileViewSet, basename='create_profile')
router.register('login', LoginViewSet, basename="login")
router.register('update-password', UpdatePasswordViewSet,
                basename='updated-password')
router.register('update-language', UpdateLanguage, basename='language')

urlpatterns = [
    path('', include(router.urls), name='auth'),
    path('user/<str:field>:<str:value>/available/',
         userExists, name='user-exists'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

# urlpatterns += router.urls
