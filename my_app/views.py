from django.shortcuts import render
from my_app.models import Item
from django.db.models import Avg, Min, Max, Count

def index_view(request):

    max_price = Item.objects.aggregate(max_value=Max('price'))
    min_price = Item.objects.aggregate(min_value=Min('price'))
    avg_price = Item.objects.aggregate(avg_price=Avg('price'))
    count_of_objects = Item.objects.all().count()
    counnt_materials = Item.objects.annotate(count_m=Count('category'))
    my_prout =  Item.objects.filter(price__lte=50)
    my_prout1 = Item.objects.filter(price__gte=50)
   

    my_obj = Item.objects.order_by('name')

    # my_obj = Item.objects.all()

    context = {

        'min_price':min_price,
        'avg_price': avg_price,
        'max_price':max_price,
        'count_of_objects':count_of_objects,
        'counnt_materials':counnt_materials,
        'my_prout':my_prout,
        'my_obj':my_obj,


    }   
    
    return render(request,'index.html',context)
