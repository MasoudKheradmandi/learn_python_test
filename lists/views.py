from django.shortcuts import render,redirect
from .models import Item
# Create your views here.
def home_page(request):
    if request.method == "POST":
        my_input = request.POST.get('my_input')
        Item.objects.create(text=my_input)
        return redirect('http://127.0.0.1:8000/listview/')
    item=Item.objects.all()
    content = {
        'items':item
    }
    return render(request,'home.html',content)


def list_view(request):
    item = Item.objects.all()
    content = {
        'item':item
    }
    return render(request,'listview.html',content)