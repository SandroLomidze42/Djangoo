from django.urls import path
from . import views
urlpatterns=[
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("sandro", views.sandro, name="sandro"),
    path("Marianne", views.marianne, name="Marianne")

]