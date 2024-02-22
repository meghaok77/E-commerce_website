from django.shortcuts import render,redirect
from django.http import HttpResponse
from adminapp.models import *
from userapp.models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError




def index1(request):
    return render(request,'index1.html')

def index(request):
    return render(request,'index.html')

def displayuser(request):
    n=userdetails.objects.all()
    context={
        'n':n
    }
    
    return render(request,'displayuser.html',context)

def addcategory(request):
    if request.method=="POST":
        n=request.POST['cname']
        im=request.FILES.get('image')
        category.objects.create(
            category_name=n,
            category_image=im

        )
    return render(request,"addcategory.html")

def displaycategory(request):
    n=category.objects.all()
    context={
        'n':n
    }

    return render(request,"displaycategory.html",context)
def editcategory(request,catid):
    n=category.objects.filter(id=catid)
    context={
        'n':n
    }
    return render(request,"editcategory.html",context)

def updatecategory(request,catid):
    if request.method=="POST":
        n=request.POST['cname']
        try:
            img_c=request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img_c.name,img_c)
        except MultiValueDictKeyError:
            file=category.objects.get(id=catid).category_image


        category.objects.filter(id=catid).update(
            category_name=n,
            category_image=file
        )
        return redirect('displaycategory')
    return render(request,"updatecategory.html")

def deletecategory(request,catid):
    category.objects.filter(id=catid).delete()
    return redirect('displaycategory')

def addproduct(request):
    categories = category.objects.all()
    context = {
        'categories':categories,
    }

    if request.method == "POST":
        pc=request.POST['pcategory']
        pn=request.POST['pname']
        pi=request.FILES.get('image')
        pd=request.POST['description']
        pp=request.POST['price']




        product.objects.create(
            product_category = category.objects.get(id=pc),
            product_name=pn,
            product_image=pi,
            product_description=pd,
            product_price=pp


        )
    return render(request,"addproduct.html", context)



def displayproduct(request):
    n=product.objects.all()
    context={
        'n':n
    }

    return render(request,"displayproduct.html",context)


def editproduct(request,pid):

    c=category.objects.all()
    categoryid=product.objects.get(id=pid).product_category

    

    n=product.objects.filter(id=pid)
    context={
        'n':n,
        'c':c,
        'categoryid':categoryid
    }
    

    return render(request,"editproduct.html",context)

def updateproduct(request,pid):
    if request.method=="POST":
        pc=request.POST['pcategory']
        pn=request.POST['pname']
        pd=request.POST['description']
        pp=request.POST['price']
        
        
        try:
            img_c = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = product.objects.get(id=pid).product_image


        product.objects.filter(id=pid).update(
        product_category=pc,
        product_name=pn,
        product_description=pd,
        product_price=pp,
        product_image=file

        )

        return redirect('displayproduct')
    
    return render(request,"editproduct.html")

def deleteproduct(request,pid):
    product.objects.filter(id=pid).delete()
    return redirect("displayproduct")

def displayfeedback(request):
    n=Contact.objects.all()
    context={
        'n':n
    }
    return render(request,"displayfeedback.html",context)

def displayreview(request):
    n=Review.objects.all()
    context={
        'n':n
    }

    return render(request,"displayreview.html",context)

def displayorders(request):
    return render(request,"displayorders.html")






    
    
   
       



# Create your views here.
