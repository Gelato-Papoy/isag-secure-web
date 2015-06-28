from django.shortcuts import render
from form import messageForm
from models import Messages
from django.http import HttpResponse
from django.utils import timezone

# Create your views here.
def postMessage(request):
    if request.method == 'POST':
        msgDB = Messages()
        msgDB.user = request.POST['user']
        msgDB.talk = request.POST['talk']
        msgDB.message = request.POST['message']
        msgDB.time = timezone.now()
        msgDB.save()
        return HttpResponse("good")# Redirect after POST
    # else:
    #     form = ContactForm() # An unbound form

    # return render(request, 'contact.html', {
    #     'form': form,
    # })
def chatbox(request):
    # template = loader.get_template("chatbox.html")
    # return HttpResponse(template.render())
    return render(request,'chater/chatbox.html')