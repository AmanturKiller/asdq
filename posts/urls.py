from django.urls import path
from . import views

urlpatterns = [
    path('publications/', views.PublicationList.as_view(), name='publication-list'),
    path('publications/<int:pk>/', views.PublicationDetail.as_view(), name='publication-detail'),
]