from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    path("accounts/", include('Accounts.urls')),
    path("book/", include('Book.urls')),
    path("choice/", include('CityChoice.urls')),
]
