from django.urls import path
from adminapp import views

urlpatterns=[
    path('index1',views.index1,name="index1"),
    path('index',views.index,name="index"),
    path('display',views.displayuser,name="displayuser"),
    path('category',views.addcategory,name="addcategory"),
    path('displaycategory',views.displaycategory,name="displaycategory"),
    path('editcategory/<int:catid>',views.editcategory,name="editcategory"),
    path('updatecategory/<int:catid>',views.updatecategory,name="updatecategory"),
    path('deletecategory/<int:catid>',views.deletecategory,name="deletecategory"),
    path('addproduct',views.addproduct,name="addproduct"),
    path('displayproduct',views.displayproduct,name="displayproduct"),
    path('updateproduct/<int:pid>',views.updateproduct,name="updateproduct"),
    path('editproduct/<int:pid>',views.editproduct,name="editproduct"),
    path('deleteproduct/<int:pid>',views.deleteproduct,name="deleteproduct"),
    path('displayfeedback',views.displayfeedback,name="displayfeedback"),
    path('displayreview',views.displayreview,name="displayreview"),
    path('displayorders',views.displayorders,name="displayorders")
]