from django.urls import path, include
from .views import hello_world
from .views import protegido
from .viewsets import AuthViewSet, TaskViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'auth', AuthViewSet, basename='auth')
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('hello/', hello_world),
    path('api/protegido/', protegido,name='protegido'),
    path('', include(router.urls)),
]
