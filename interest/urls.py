from django.urls import path
from . import views

urlpatterns = [
    path("", views.tags_index, name="tags_index"),
    path("<int:pk>/", views.link_detail, name="link_detail"),
]
