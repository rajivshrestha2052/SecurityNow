from django.urls import path

from .views import GuardProfileView


urlpatterns = [
    path(
        "profile/",
        GuardProfileView.as_view(),
        name="guard-profile",
    ),
]