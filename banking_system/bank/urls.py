from django.urls import path
from . import views
app_name="BankApp"
urlpatterns=[
    path("",views.home,name="home1"),
    path("Home.html",views.home,name="home"),
    path("Customer-List.html",views.userlist,name="customer"),
    path("Transaction-History.html",views.transaction,name="transaction"),
    path("info/Transaction-History.html",views.info2,name="info2"),
    path("info/Customer-List.html",views.userlist,name="ul2"),
    path("info/<str:id>",views.info,name="info"),

]