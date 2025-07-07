from django.urls import path
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
from Accounts.views import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

# from Accounts.views import token_details

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # Refresh
    # path('token_details/', token_details, name='token_details'),
]