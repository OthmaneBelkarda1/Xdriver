from django.urls import path
from . import views

urlpatterns = [
   path('book_ride/', views.Book_Ride, name='book_ride'),
   path('ride_history/<str:passenger_id>', views.viewRideHistoryByID, name='ride_history')
]
