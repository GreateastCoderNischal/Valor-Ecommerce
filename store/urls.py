from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='home'),
    path("cart/", views.cart, name="cart"),
    path("checkout/",views.checkout,name='checkout'),
    path('update-item/',views.updateItem,name='update-item')
]