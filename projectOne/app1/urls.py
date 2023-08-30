from django.urls import path
from . import views
urlpatterns=[
    path("", views.index, name="index"),
    path("sandro", views.sandro, name="sandro"),
    path("Marianne", views.marianne, name="Marianne")
]