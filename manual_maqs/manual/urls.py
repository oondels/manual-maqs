from django.urls import path
from .views import manual_maquinas_view

urlpatterns = [
    path('manual_maquinas/', manual_maquinas_view, name='manual_maquinas'),
]
