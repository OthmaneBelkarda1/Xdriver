from django.urls import path
from . import views

urlpatterns = [
   path('publish_Ride/', views.publish_Ride, name='publish_Ride'),
   path('ride-history/<int:id>/', views.viewRideHistory, name='ride-history'),
   path('search/<str:departure>/<str:arrival>/<str:date>/', views.SearchForRide, name='search-ride'),
   path('delete_ride/', views.delete_ride, name='delete_ride'),
   path('edit_ride/', views.edit_ride, name='edit_ride'),
]
