from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.template import loader, RequestContext


def login(request):
    # import ipdb;ipdb.set_trace()
    template = loader.get_template('chater/login.html')

    return render(request,'chater/login.html')
    #return render(request,)
    # return HttpResponse("Hello, world. You're at the polls index.")
    # username = request.POST['username']
    # password = request.POST['password']
    # user = authenticate(username='admin', password='admin')
    # if user is not None:
    #     # the password verified for the user
    #     if user.is_active:
    #         return HttpResponse("User is valid, active and authenticated")
    #     else:
    #         return HttpResponse("The password is valid, but the account has been disabled!")
    # else:
    #     # the authentication system was unable to verify the username and password
    #     return HttpResponse("The username and password were incorrect.")



def register(request):
    user = User.objects.create_user('test2', '', 'test2')
    user.save()
    return HttpResponse("register success!")


#def listMessage(request):
#    latest_messages_list = Messages.objects.order_by('-pub_date')
#    output = ', '.join([p.question_text for p in latest_messages_list])
#    return HttpResponse(output)
