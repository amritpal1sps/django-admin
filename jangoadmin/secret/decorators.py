from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from django.shortcuts import render,redirect

# NOT IN USE CURRENTLY
def my_login_required(function):
   def wrap(request, *args, **kwargs):
      # check some condition here
      if request.session['name'] :
         return function(request, *args, **kwargs)
      else:
         return render(request, 'secret/login.html')
         raise PermissionDenied
   wrap.__doc__ = function.__doc__
   wrap.__name__ = function.__name__
   return wrap


# NOT IN USE CURRENTLY
def superadmin_required(function):
   def wrap(request, *args, **kwargs):
      # check some condition here
      if request.session['role'] == "SuperAdmin":
         return function(request, *args, **kwargs)
      else:
         raise PermissionDenied
   wrap.__doc__ = function.__doc__
   wrap.__name__ = function.__name__
   return wrap
