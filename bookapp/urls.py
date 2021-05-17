"""bookproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import create_book,list_all_book,book_details,delete_book,edit_book,regstration,login_user,signout,BookList,BookCreate,Bookdetail,Bookupdate,Bookdelete

urlpatterns = [
    path('create',create_book,name="createbook"),
    path('list',list_all_book,name="listbook"),
    path('detail/<int:id>',book_details,name="details"),
    path('delete/<int:id>',delete_book,name="delete"),
    path('edit/<int:id>',edit_book,name="edit"),
    path('reg/',regstration,name="registration"),
    path('login/',login_user,name="userlogin"),
    path('logout/',signout,name="signout"),
    path('books',BookList.as_view(),name="books"),
    path('bookcreate',BookCreate.as_view(),name="cbook"),
    path('books/<int:pk>',Bookdetail.as_view(),name="bookdetail"),
    path('books/edit/<int:pk>',Bookupdate.as_view(),name="bookedit"),
    path('books/delete/<int:pk>',Bookdelete.as_view(),name="bookdelete"),

]
