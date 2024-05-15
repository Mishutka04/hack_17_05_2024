from django.urls import path
from .views import (
    LineListAPIView,
    NegotiationListCreateAPIView,
    ReferenceDialogListAPIView
    )


app_name = "conversation"
urlpatterns = [
    path(
        'lines/',
        LineListAPIView.as_view(),
        name='line-list'),
    path(
        'dialogs/',
        ReferenceDialogListAPIView.as_view(),
        name='dialog-list'),
    path(
        'negotiations/',
        NegotiationListCreateAPIView.as_view(),
        name='negotiation-list-create'),
]
