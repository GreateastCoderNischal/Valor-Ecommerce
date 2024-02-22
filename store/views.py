from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
# Create your views here.
def index(request):
   
    order,create=Order.objects.get_or_create(complete=False)
    total=order.total_items
    context={
        'products':Product.objects.all(),
        'total':total,
    }
    return render(request,"index.html",context)

def cart(request):
    customer=request.user.customer
    order,created=Order.objects.get_or_create(customer=customer,complete=False)
    items=order.orderitem_set.all()
    print(items)
    total_item=order.total_items
    context={
        'items':items,
        'order':order,
        'total':total_item,
    }
    return render(request,"cart.html",context)
    

def checkout(request):
    order,create=Order.objects.get_or_create(complete=False)
    total=order.total_items
    customer=request.user.customer
    order,created=Order.objects.get_or_create(customer=customer,complete=False)
    print(order)
    items=order.orderitem_set.all()
    print(items)
    context={
        'items':items,
        'order':order,
        'total':total,
    }
    return render(request,"checkout.html",context)

def updateItem(request):

    data=json.loads(request.body)
    print(data)
    print(data['id'])
    customer=request.user.customer
    order,created=Order.objects.get_or_create(customer=customer,complete=False)
    orderItem,option2=OrderItem.objects.get_or_create(order=order,product=Product.objects.get(id=data['id']))
    if data['action']=='add':
        orderItem.quantity=(orderItem.quantity+1)
    elif data['action']=='remove':
        orderItem.quantity-=1
    orderItem.save()
    if orderItem.quantity<=0:
        orderItem.delete()
        
    return JsonResponse(
        'hello Namaste'
    ,safe=False)