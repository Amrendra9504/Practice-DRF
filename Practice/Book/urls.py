from django.urls import path
from Book.views import AuthorList, AuthorDetails, BookList
urlpatterns = [
    path('author/', AuthorList.as_view(), name='author-list'),
    path('authordetails/<int:pk>', AuthorDetails.as_view(), name='author-details'),
    path('books/', BookList.as_view(), name='books-list'),
]