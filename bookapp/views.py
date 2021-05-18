from django.shortcuts import render,redirect
from .forms import BookCreateForm
from .models import Book
from .forms import UserRegistrationForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from .decorators import login_loginrequired,admin_only
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView,TemplateView
from django.urls import reverse_lazy, reverse


# Create your views here.

# def login_loginrequired(func):
#     def wrapper(request,*args,**kwargs):
#         if not request.user.is_authenticated:
#             return redirect("userlogin")
#         else:
#             return func(request,*args,**kwargs)
#         return wrapper

@admin_only
def create_book(request):
    # if request.user.is_authenticated:
        form=BookCreateForm()
        context={}
        context["form"]=form
        # if request.method=='POST':
        #     form=bookCreateForm(request.POST)
        #     if form.is_valid():
        #         bname=form.cleaned_data.get("book_name")
        #         author=form.cleaned_data.get("author")
        #         price=form.cleaned_data.get("price")
        #         pages=form.cleaned_data.get("pages")
        #         book=Book(book_name=bname,author=author,price=price,pages=pages)
        #         book.save()
        #         print(bname,author,price,pages)
        #         return redirect("listbook")
        #     else:
        #         pass
        return render(request,"bookapp/createbook.html",context)
    # else:
    #     return redirect("userlogin")

@login_loginrequired
def list_all_book(request):
    books=Book.objects.all()
    context={}
    context["books"]=books

    return render(request,"bookapp/listallbook.html",context)

# @login_loginrequired
def book_details(request,id):
    book=Book.objects.get(id=id)
    context={}
    context["book"]=book
    return render(request,"bookapp/bookdetails.html",context)

@admin_only
def delete_book(request,id):
    book=Book.objects.get(id=id)
    book.delete()
    return redirect("listbook")

@admin_only
def edit_book(request,id):
    book=Book.objects.get(id=id)
    form=BookCreateForm(instance=book)
    context={}
    context["form"]=form
    if request.method=='POST':
        form=BookCreateForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect("listbook")
    return render(request,"bookapp/editbook.html",context)

def regstration(request):
    form=UserRegistrationForm()
    context={}
    context["form"]=form
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"bookapp/login.html")
        else:
            form=UserRegistrationForm(request.POST)
            context["form"]=form
            return redirect("userlogin")

    return render(request,"bookapp/registration.html",context)

def login_user(request):
    form=LoginForm()
    context={}
    context["form"]=form
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return render(request,"bookapp/index.html")

    return render(request,"bookapp/login.html",context)

def signout(request):
    logout(request)
    return redirect("userlogin")



# class based view creating


#customizing built in views

# class ObjectMixin():
#     model=None
#     def get_object(self,id):
#         return self.model.objects.get(id=id)

class Listbook(TemplateView):
    model=Book
    template_name = "bookapp/listallbook.html"
    context={}
    def get(self, request, *args, **kwargs):
        books=self.model.objects.all()
        self.context["books"]=books
        return render(request,self.template_name,self.context)

class Createbook(TemplateView):
    model=Book
    template_name = "bookapp/createbook.html"
    context={}
    form_class=BookCreateForm
    def get(self, request, *args, **kwargs):
        self.context["form"]=self.form_class()
        return render(request,self.template_name,self.context)
    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("templbooks")
        else:
            self.context["form"]=form
            return render(request, self.template_name, self.context)

    def get_object(self,id):
         return self.model.objects.get(id=id)

class Detailbook(TemplateView):
    model=Book
    template_name = "bookapp/bookdetails.html"
    context={}
    def get(self, request, *args, **kwargs):
        print(kwargs)
        id=kwargs.get("pk")
        books=self.model.objects(id)
        self.context["book"]=books
        return render(request,self.template_name,self.context)

class Updatebook(TemplateView):
    model=Book
    template_name = "bookapp/editbook.html"
    form_class=BookCreateForm
    context={}
    lookup=0
    def get_object(self,id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        self.lookup=kwargs.get("pk")
        book=self.get_object(self.lookup)
        form=self.form_class(instance=book)
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request,**kwargs):
        self.lookup = kwargs.get("pk")
        print(kwargs)
        book = self.get_object(self.lookup)
        form=self.form_class(instance=book,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("templbooks")
        else:
            self.context["form"] = form
            return render(request, self.template_name, self.context)

class Deletebook(TemplateView):
    model=Book
    def get_object(self,id=id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        id=kwargs.get("pk")
        book=self.get_object(id)
        book.delete()
        return redirect("templbooks")

#django built in views

class BookList(ListView):
    model = Book
    template_name = "bookapp/listallbook.html"
    context_object_name = "books"

class BookCreate(CreateView):
    model = Book
    template_name = "bookapp/createbook.html"
    form_class = BookCreateForm
    success_url = reverse_lazy("books")
    # def get_success_url(self):
    #     return reverse("books")          #  <<< second method

class Bookdetail(DetailView):
    model = Book
    template_name = "bookapp/bookdetails.html"
    context_object_name = "book"

class Bookupdate(UpdateView):
    model = Book
    form_class = BookCreateForm
    template_name = "bookapp/editbook.html"
    success_url = reverse_lazy("books")

class Bookdelete(DeleteView):
    model = Book
    template_name = "bookapp/deletebook.html"
    context_object_name = "book"
    success_url = reverse_lazy('books')