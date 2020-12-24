from django.shortcuts import render, redirect
from django.http import HttpResponse
from index.views import login
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .PayTm import Checksum
MERCHANT_KEY = 'M7#Mx01Fjjg3AK6%'

# Create your views here.
@login_required(login_url="/login/")
def home_index(request):
    if request.user.groups.exists():
        ls = request.user.groups.all()[0].name
        if ls == 'c11th':
            return redirect('c11th')
        if ls == 'c12th':
            return redirect('c12th')
        if ls == 'b1st':
            return redirect('b1st')
        if ls == 'b2nd':
            return redirect('b2nd')
        if ls == 'b3rd':
            return redirect('b3rd')
    return render(request, 'home/index.html')

@login_required(login_url="/login/")
def c11th(request):
    ls = request.user.groups.all()[0].name
    if ls == 'c11th':
        return HttpResponse('class11')
    else:
        return redirect('home_index')
    
@login_required(login_url="/login/")
def c12th(request):
    ls = request.user.groups.all()[0].name
    if ls == 'c12th':
        return HttpResponse('class12')
    else:
        return redirect('home_index')

@login_required(login_url="/login/")
def b1st(request):
    ls = request.user.groups.all()[0].name
    if ls == 'b1st':
        return HttpResponse('B.Com 1st year')
    else:
        return redirect('home_index')

@login_required(login_url="/login/")
def b2nd(request):
    ls = request.user.groups.all()[0].name
    if ls == 'b2nd':
        return HttpResponse('B.Com 2nd year')
    else:
        return redirect('home_index')

@login_required(login_url="/login/")
def b3rd(request):
    ls = request.user.groups.all()[0].name
    if ls == 'b3rd':
        return HttpResponse('B.Com 3rd year')
    else:
        return redirect('home_index')

@login_required(login_url="/login/")
def payments(request):
    if request.method == 'POST':
        data_dict = {
            'MID':'GaVogD70606004927811',
            'ORDER_ID':'043',
            'TXN_AMOUNT':'499',
            'CUST_ID':request.user.email,
            'INDUSTRY_TYPE_ID':'Retail',
            'WEBSITE':'WEBSTAGING',
            'CHANNEL_ID':'WEB',
	        'CALLBACK_URL':'http://127.0.0.1:8000/home/handlerequest/'
        }
        param_dict = data_dict  
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(data_dict, MERCHANT_KEY)
        return render(request, 'home/paytm.html', {'param_dict':param_dict})
    return render(request, 'home/checkout.html')

@csrf_exempt
def handleRequest(request):
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print("Order Successfull")
        else:
            print("Order was not successfull because" + response_dict['RESPMSG'])
    return render(request, 'home/paymentstatus.html', {'response':response_dict})

@login_required(login_url="/login/")
def add_in_a_class(request):
    if request.method == 'POST':
        groupe = request.POST['class_batch']

        if groupe == 'b2nd':
            group = Group.objects.get(name = 'b2nd')
            request.user.groups.add(group)
        
        if groupe == 'b1st':
            group = Group.objects.get(name = 'b1st')
            request.user.groups.add(group)
        
        if groupe == 'b3rd':
            group = Group.objects.get(name = 'b3rd')
            request.user.groups.add(group)
        
        if groupe == 'c11th':
            group = Group.objects.get(name = 'c11th')
            request.user.groups.add(group)
        
        if groupe == 'c12th':
            group = Group.objects.get(name = 'c12th')
            request.user.groups.add(group)
        return redirect('home_index')
    else:
        return redirect('payments')