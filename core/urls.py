from django.urls import path
from .views import hello_world
from .views import protegido

urlpatterns = [
    path('hello/', hello_world),
    path('api/protegido/', protegido,name='protegido')
]
