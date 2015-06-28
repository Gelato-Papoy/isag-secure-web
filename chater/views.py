from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate

# class UserLogin:
#     def __init__(self,request):
#         print "AAAA"
#         HttpResponse("Hello, world. You're at the polls index.")
#

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    user = authenticate(username='admin', password='admin')
    if user is not None:
        # the password verified for the user
        if user.is_active:
            return HttpResponse("User is valid, active and authenticated")
        else:
            return HttpResponse("The password is valid, but the account has been disabled!")
    else:
        # the authentication system was unable to verify the username and password
        return HttpResponse("The username and password were incorrect.")
