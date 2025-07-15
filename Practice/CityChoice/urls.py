from django.urls import path
from CityChoice.views import CityList
urlpatterns = [
    path('city/', CityList.as_view(), name='city-list'),
    # path('authordetails/<int:pk>', AuthorDetails.as_view(), name='author-details'),
    # path('books/', BookList.as_view(), name='books-list'),
]