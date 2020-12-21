from django.http import HttpResponse
from django.shortcuts import redirect


def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):

			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name

			if group in allowed_roles:
				return view_func(request, *args, **kwargs)
			else:
				return HttpResponse('You are not authorized to view this page')
		return wrapper_func


def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        
        if group == 'b1st':
            return redirect('b1st')
        
        if group == 'b2nd':
            return redirect('b2nd')
        
        if group == 'b3rd':
            return redirect('b3rd')
        
        if group == 'c11th':
            return redirect('c11th')
        
        if group == 'c12th':
            return redirect('c12th')

    return wrapper_function