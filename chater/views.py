from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from models import Messages
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.template import loader, RequestContext
from chater.models import Messages

def index(request):
    return render(request,'chater/index.html')

def postMessage(request):
    if request.method == 'POST':
        msgDB = Messages()
        msgDB.user = request.POST['user']
        msgDB.talk = request.POST['talk']
        msgDB.message = request.POST['message']
        msgDB.time = timezone.now()
        msgDB.save()
        return HttpResponseRedirect("/listmsg/")# Redirect after POST
    # else:
    #     form = ContactForm() # An unbound form
    # return render(request, 'contact.html', {
    #     'form': form,
    # })
def chatbox(request):
    # template = loader.get_template("chatbox.html")
    # return HttpResponse(template.render())
    return render(request,'chater/chatbox.html')

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
            return redirect('/listmsg/')
        else:
            return HttpResponse("The password is valid, but the account has been disabled!")
    else:
        # the authentication system was unable to verify the username and password
        return HttpResponse("The username and password were incorrect.<br><br><a href=\"/\"><button>LOGIN</button></a>")

def logout(request):
    del request.session['user_id']
    return redirect('/logoutsuccess/')

def logoutsuccess(request):
    return render(request,'chater/logout.html')

def register(request):
    return render(request,'chater/register.html')

def registersuccess(request):
    usr = request.POST['username']
    passwd = request.POST['password']
    user = User.objects.create_user(usr, '', passwd)
    user.save()
    return redirect('/')

def listMessage(request):
    u = User.objects.get(id=request.session['user_id'])
    latest_msg_list = Messages.objects.filter(talk=u.username)
    template = loader.get_template('chater/listmessage.html')
    context = RequestContext(request, {
        'latest_message_list': latest_msg_list,
        'me': u.username,
    })
    return HttpResponse(template.render(context))
    
def about(request):
    return render(request,'chater/about.html')
