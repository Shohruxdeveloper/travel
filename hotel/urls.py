from django.urls import path
from .views import (TravelAPIView, TravelDetailAPIView, HotelAPIView, HotelDetailAPIView,
                    KlassAPIView, KlassDetailAPIView)


urlpatterns = [
    path('api/v1/', TravelAPIView.as_view()),
    path('api/v1/<int:pk>/', TravelDetailAPIView.as_view()),
    path('api/v2/', HotelAPIView.as_view()),
    path('api/v2/<int:pk>/', HotelDetailAPIView.as_view()),
    path('api/v3/', KlassAPIView.as_view()),
    path('api/v3/<int:pk>/', KlassDetailAPIView.as_view()),
]
