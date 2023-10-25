from django.shortcuts import render
from my_app.views import Item

def index_view(request):

    my_obj = Item.objects.all()

    context = {

        'my_obj':my_obj
    }
    
    return render(request,'index.html',context)
