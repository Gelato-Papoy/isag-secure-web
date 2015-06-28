from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.template import loader, RequestContext


def login(request):
    return render(request,'chater/login.html')
    #return render(request,)
    # return HttpResponse("Hello, world. You're at the polls index.")

def loginsuccess(request):
    usr = request.POST['username']
    passwd = request.POST['password']
    user = authenticate(username=usr, password=passwd)
    if user is not None:
        # the password verified for the user
        if user.is_active:
            u = User.objects.get(username=usr)
            request.session['user_id'] = u.id
            print request.session['user_id']
            return HttpResponse("Hello %s" % usr)
        else:
            return HttpResponse("The password is valid, but the account has been disabled!")
    else:
        # the authentication system was unable to verify the username and password
        return HttpResponse("The username and password were incorrect.")

def logout(request):
    del request.session['user_id']
    return HttpResponse("You're logged out.")

def register(request):
    print request.session['user_id']
    return render(request,'chater/register.html')

def registersuccess(request):
    usr = request.POST['username']
    passwd = request.POST['password']
    user = User.objects.create_user(usr, '', passwd)
    user.save()
    return HttpResponse("register success!")

#def listMessage(request):
#    latest_messages_list = Messages.objects.order_by('-pub_date')
#    output = ', '.join([p.question_text for p in latest_messages_list])
#    return HttpResponse(output)
