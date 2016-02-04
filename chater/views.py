from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from models import Messages
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth import authenticate
from django.template import loader, RequestContext
from chater.models import Messages
# from .forms import UploadFileForm
import os, tempfile, zipfile, mimetypes
# from django.core.servers.basehttp import FileWrapper
from django.core.files.base import ContentFile
from django.utils.six import b
from django.core.files import File
from django.utils.encoding import smart_str

def index(request):
    return render(request,'chater/index.html')

def downloadFile(request):
    if request.method == 'GET':
        filename = request.GET['file_name']
        download_name = filename[10:]
        # ipdb.set_trace()
        download_file = File.open(filename)
        content_type = mimetypes.guess_type(filename)[0]
        response     = HttpResponse(download_file,content_type=content_type)
        response['Content-Length']      = os.path.getsize(filename)    
        response['Content-Disposition'] = "attachment; filename=%s"%download_name
        response['X-Sendfile'] = smart_str(filename)
        return response

def postMessage(request):
    if request.method == 'POST':
        msgDB = Messages()
        msgDB.user = request.POST['user']
        msgDB.talk = request.POST['talk']
        msgDB.message = request.POST['message']
        msgDB.time = timezone.now()
        # form = UploadFileForm(request.POST, request.FILES)
        # if form.is_valid():
        # print request.FILES['file']
        # ipdb.set_trace()
        msgDB.file_path = request.FILES['file']
        # instance = ModelWithFileField(file_field=request.FILES['file'])
        # form = UploadFileForm(request.POST, request.FILES)
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
    # import ipdb;ipdb.set_trace()
    if not request.session.is_empty():
        return redirect("/listmsg")
    else:
        return render(request,'chater/login.html')
    #return render(request,)
    # return HttpResponse("Hello, world. You're at the polls index.")

def loginsuccess(request):
    # import ipdb;ipdb.set_trace()
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
    # import ipdb;ipdb.set_trace()
    if not request.session.is_empty():
        request.session.delete()
        return redirect('/logoutsuccess/')

    else:
        return redirect('/login/')

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
    if not request.session.is_empty() or request.user.is_anonymous():
        u = User.objects.get(id=request.session['user_id'])
        latest_msg_list = Messages.objects.filter(talk=u.username)
        template = loader.get_template('chater/listmessage.html')
        context = RequestContext(request, {
            'latest_message_list': latest_msg_list,
            'me': u.username,
        })
        return HttpResponse(template.render(context))
    else:
        return redirect('/login/')
    
def about(request):
    return render(request,'chater/about.html')

def usrSetting(request):
    if not request.session.is_empty() or request.user.is_anonymous():
        u = User.objects.get(id=request.session['user_id'])
        latest_msg_list = Messages.objects.filter(talk=u.username)
        template = loader.get_template('chater/setting.html')
        context = RequestContext(request, {
            'latest_message_list': latest_msg_list,
            'me': u.username,
        })
        return HttpResponse(template.render(context))
    else:
        return redirect('/login/')

def changePassword(request):
    if request.method == 'POST':
        cuurentUser = request.POST['user']
        oldPassword = request.POST['oldpwd']
        newPassword = request.POST['newpwd']
        user = authenticate(username=cuurentUser, password=oldPassword)
        if user.is_active:
            print("Authenticate")
            u = User.objects.get(username=cuurentUser)
            u.set_password(newPassword)
            u.save()
            return HttpResponseRedirect("/service/setting/" )
        else:
            print("Password not valid")            
       
