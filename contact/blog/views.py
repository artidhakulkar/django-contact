from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from.models import Contact

# Create your views here.

def contact(request):
    if request.method == "POST":
        email = request.POST.get('email', "")
        print(email)
        c = Contact(email=email)
        c.save()
    return render(request, "blog/contact.html")



