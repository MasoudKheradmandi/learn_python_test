from django.shortcuts import render
from .models import Item
# Create your views here.
def home_page(request):
    if request.method == "POST":
        my_input = request.POST.get('my_input')
        Item.objects.create(text=my_input)
    content = {

    }
    return render(request,'home.html',content)


def home_number2(request):
    pass