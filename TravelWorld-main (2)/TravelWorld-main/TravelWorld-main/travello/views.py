from django.shortcuts import render , redirect
from .models import Destination


# Create your views here.

def index(request):
    if request.method =="POST":
        name=request.POST["name"]
        img = request.POST["img"]
        desc = request.POST["desc"]
        price = request.POST["price"]
        offer = request.POST["offer"]


        dests = Destination.objects.all()

        data = Destination(name=name,img=img,desc=desc,price=price,offer=offer)
        data.save()
        return redirect("index")
    else:
        return render(request, 'index.html',)

