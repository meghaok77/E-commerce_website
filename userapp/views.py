from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from userapp.models import *
from adminapp.models import *
from django.db.models import Avg
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

def userindex1(request):
    uid=request.session.get('uid')
    count=Cart.objects.filter(uid=uid).count()
    context={
        'count':count

    }
  
    return render(request,"userindex1.html",context)

def usercategory(request):
    print("---------------------------")
    uid=request.session.get('uid')
    n=category.objects.all()
    n2=product.objects.all()
    count=Cart.objects.filter(uid=uid).count()
    
    context={
        'n':n,
        'n2':n2,
        'count':count
    }

    return render(request,"usercategory.html",context)



def userdisplaycategory(request,cid):
    uid=request.session.get('uid')
    count=Cart.objects.filter(uid=uid).count()
    

    n=product.objects.filter(product_category=cid)
    context={
        'n':n,
        'count':count
            }
    

    return render(request,"userdisplaycategory.html",context)

def adminlogin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        if email == "admin@gmail.com" and password == "admin":
            return redirect("index")
        else:
            return HttpResponse("Invalid details")
    return render(request,"adminlogin.html")

def userlogin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        if userdetails.objects.filter(email = email, password = password).exists():
            data = userdetails.objects.filter(email = email, password = password).values('id','first_name', 'last_name', 'address','email').first()
            request.session['f_name'] = data['first_name']
            request.session['l_name'] = data['last_name']

            request.session['address'] = data['address']
            request.session['uid'] = data['id']
            request.session['email'] = data['email']
            return redirect('usercategory')
        
        else:
            return HttpResponse("Invalid details")

    return render(request,"userlogin.html")

def userregister(request):

    if request.method == "POST":
        fn=request.POST['fname']
        ln=request.POST['lname']
        a=request.POST['address']
        e=request.POST['email']
        p=request.POST['password']
        userdetails.objects.create(
            first_name=fn,
            last_name=ln,
            address=a,
            email=e,
            password=p
        )



    return render(request,"userregister.html")

def productdetails(request,proid):
    uid=request.session.get('uid')
    count=Cart.objects.filter(uid=uid).count()
    
    n=product.objects.filter(id=proid)
    name=request.session.get('f_name')
    email=request.session.get('email')
    reviews=Review.objects.filter(product_id=proid)
    count=Review.objects.filter(product_id=proid).count()
    avgreview=Review.objects.filter(product_id=proid).aggregate(average=Avg('rating'))
    avg=0
    avg = float (avgreview['average'])
   
    

    
    context={
        'count':count,
        'n':n,
        'name':name,
        'email':email,
        'proid':proid,
        'reviews':reviews,
        'avg':avg
        

        

    }





    return render(request,"productdetails.html",context)

def cart(request,proid):

    uid=request.session.get('uid')

    count=Cart.objects.filter(uid=uid).count()
    productdetails=product.objects.get(id=proid)
    context={
        'count':count
    }


    if request.method == 'POST':
        q=request.POST['quantity']
        print(q)
       
        print(productdetails.product_price)
        total=int(q)*int(productdetails.product_price)
     
        Cart.objects.create(
            uid=userdetails.objects.get(id=uid),
            product_id=product.objects.get(id=proid),
            quantity=q,
            total=total
            )

    return redirect("displaycart",context)


def displaycart(request):

    uid=request.session.get('uid')
    count=Cart.objects.filter(uid=uid).count()
    cartid=Cart.objects.filter(uid=uid)
    print(uid)
    l=0
    subtotal=0
    cartdetails=Cart.objects.filter(uid=uid)
    for i in cartdetails:
        l+=i.total
        print(i)
    print("total:",l)
    subtotal=l+80
            

    
       
    context={
        'cartid':cartid,
        'l':l,
        'count':count,
        'subtotal':subtotal

        
    }
    
    

    return render(request,"cart.html",context)


def deletecart(request,cid):

    Cart.objects.filter(id=cid).delete()
    return redirect("displaycart")






def productreview(request,productid):
    uid=request.session.get('uid') 
    product_id=product.objects.get(id=productid)
    if request.method == 'POST':
        review=request.POST['reviews']
        rating=request.POST['rating']
        Review.objects.create(
            uid=userdetails.objects.get(id=uid),
            product_id=product_id,
            review=review,
            rating=rating
            
        )

    
    return render(request,"productdetails.html")








def contact(request):
    uid=request.session.get('uid') 
    count=Cart.objects.filter(uid=uid).count()
    f_name=request.session.get('f_name')
    email=request.session.get('email')
    context={
        'f_name':f_name,
        'email':email,
        'count':count
    }
    if request.method == "POST":
        subject=request.POST['subject']
        message=request.POST['message']

        Contact.objects.create(
            uid=userdetails.objects.get(id=uid),
            subject=subject,
            message=message
        )


    return render(request,"contact.html",context)

def shopnow(request):
    
    n=product.objects.filter(product_category = 8)
    context={
        'n':n
    }
    return render(request,"shopnow.html",context)

def checkout(request):
    uid=request.session.get('uid')
    l=0
    subtotal=0
    cartdetails=Cart.objects.filter(uid=uid)
    for i in cartdetails:
        l+=i.total
        print(i)
    print("total:",l)
    subtotal=l+80
    context={
    'l':l,
    'subtotal':subtotal

    }
    
    return render(request,"checkout.html",context)
def placeorder(request):
    uid=request.session.get('uid')



    if request.method=="POST":
        firstname=request.POST.get('f_name')
        lastname=request.POST.get('l_name')
        address1=request.POST.get('address1')
        address2=request.POST.get('address2')
        email=request.POST.get('email')
        country=request.POST.get('country')
        city=request.POST.get('city')
        state=request.POST.get('state')
        zip=request.POST.get('zip')
        payment_mode=request.POST.get('payment')
        Paymentdetails.objects.create(
            uid=userdetails.objects.get(id=uid),
            firstname=firstname,
            lastname=lastname,
            address1=address1,
            address2=address2,
            email=email,
            country=country,
            city=city,
            state=state,
            zip=zip,
            payment_mode=payment_mode


        )


    return render(request,"checkout.html")

def adminlogin(request):

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')


        if email == "admin@gmail.com" and password == "admin123":
            return redirect('index')
        
        else:
            return HttpResponse("Invalid details")
    return render(request,"adminlogin.html")














    
















    







# Create your views here.
