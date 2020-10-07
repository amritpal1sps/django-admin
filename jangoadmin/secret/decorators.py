from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from django.shortcuts import render,redirect


# NOT IN USE CURRENTLY
def superadmin_required(function):
   def wrap(request, *args, **kwargs):
      # check some condition here
      if request.session['role'] == True:
         return function(request, *args, **kwargs)
      else:
         raise PermissionDenied
   wrap.__doc__ = function.__doc__
   wrap.__name__ = function.__name__
   return wrap
