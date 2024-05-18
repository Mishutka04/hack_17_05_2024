from django.urls import path
from .views import (
    LineListAPIView,
    NegotiationListCreateAPIView,
    ReferenceDialogListAPIView, NegotiationInfoList
)

app_name = "conversation"
urlpatterns = [
    path(
        'lines/',
        LineListAPIView.as_view(),
        name='line-list'),
    path(
        'dialogs/<int:pk>/',
        ReferenceDialogListAPIView.as_view(),
        name='dialog-list'),
    path(
        'dialogs/',
        ReferenceDialogListAPIView.as_view(),
        name='dialog-list'),

    path(
        'negotiations/',
        NegotiationListCreateAPIView.as_view(),
        name='negotiation-list-get'),
    path(
        'negotiations/<int:pk>/',
        NegotiationListCreateAPIView.as_view(),
        name='negotiation-list-get-pk'),
    path(
        'negotiations_info/<int:pk>/',
        NegotiationInfoList.as_view(),
        name='negotiation_info-list-create'),
]
