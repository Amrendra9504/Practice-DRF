from django.shortcuts import render
from rest_framework_simplejwt.tokens import AccessToken


from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# def token_details(request):
#     token_str = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUxNzE2MDUxLCJpYXQiOjE3NTE3MTU1MzYsImp0aSI6ImZmMjg3YmUxZTQwMjQzNGJiMDVhNmVlNmQ3YmI4Y2UzIiwidXNlcl9pZCI6MiwidXNlcm5hbWUiOiJhbWFydXNlciIsImVtYWlsIjoiYW1hckBnbWFpbC5jb20ifQ.4g726gJe1KCTBH8vlN2Y37BuaLajYsHMxUMLzET828I'
#       # Decode the token
#     token = AccessToken(token_str)

#     # Access details from the payload
#     user_id = token['user_id']     # Default key
#     exp = token['exp']             # Expiration time (Unix timestamp)

#     print("User ID:", user_id)
#     print("Expires at:", exp)

#     import pdb
#     pdb.set_trace()

