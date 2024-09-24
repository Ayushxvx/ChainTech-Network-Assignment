from django.urls import path
from .views import *

urlpatterns =[
    path("",index,name="index"),
    path("formAdd",form,name="form"),
    path("showUser",showUser,name="showUser"),
    path("<str:anything>",anything,name="anything")
]