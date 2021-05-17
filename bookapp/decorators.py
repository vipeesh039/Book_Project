from django.shortcuts import redirect


def login_loginrequired(func):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
             return redirect("userlogin")
        return func(request,*args,**kwargs)
    return wrapper

def admin_only(func):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_superuser:
             return redirect("userlogin")
        return func(request,*args,**kwargs)
    return wrapper