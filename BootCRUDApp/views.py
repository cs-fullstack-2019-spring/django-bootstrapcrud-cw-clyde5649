from django.shortcuts import render,redirect
from .forms import GarageSellmodel,GarageSellform

# Create your views here.
def index(request):
    allEntries = GarageSellmodel.objects.all()
    context = {
        "allEntries": allEntries
    }
    return render(request, 'BootCRUDApp/index.html', context)



def garage(request):
    form = GarageSellform(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("index")
    context = {
        "form": form
    }
    return render(request,'BootCRUDApp/garage.html',context)


def edit(request):
    return render(request,'BootCRUDApp/edit.html')