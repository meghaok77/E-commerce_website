from django.urls import path
from userapp import views

urlpatterns=[
    path('userindex1',views.userindex1,name="userindex1"),
    path('',views.usercategory,name="usercategory"),
    path('userdisplaycategory/<int:cid>',views.userdisplaycategory,name="userdisplaycategory"),
    path('adminlogin',views.adminlogin,name="adminlogin"),
    path('userlogin',views.userlogin,name="userlogin"),
    path('userregister',views.userregister,name="userregister"),
    path('productdetails/<int:proid>',views.productdetails,name="productdetails"),
    path('cart/<int:proid>',views.cart,name="cart"),
    path('displaycart',views.displaycart,name="displaycart"),
   
    path('deletecart<int:cid>',views.deletecart,name="deletecart"),
    path('productreview/<int:productid>',views.productreview,name="productreview"),
    path('contact',views.contact,name="contact"),
    path('shopnow',views.shopnow,name="shopnow"),
    path('checkout',views.checkout,name="checkout"),
    path('placeorder',views.placeorder,name="placeorder")
    

    
    
    
]