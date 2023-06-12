from django.shortcuts import render, HttpResponse,redirect
from Home.models import SignUp,Customer_Support
from Home.models import Orders
from Home.models import OrderUpdate
from django.contrib.auth import authenticate, login
from math import ceil
import json
from django.views.decorators.csrf import csrf_exempt
from Paytm import Checksum
from django.http import HttpResponse
MERCHANT_KEY = 'Your-Merchant-Key-Here'


def index(request):
    return render(request,'Home.html')

def About(request):
    return render(request,'About.html')

def FAQ(request):
    return render(request,'FAQ.html')

def Login(request):
    if request.method == 'POST':
           Name = request.POST.get('Name')
           Email=request.POST.get('Email')
           Password = request.POST.get('Password')
           user = authenticate(request,Name=Name, Email=Email, Password= Password)
           if user is not None:
               login(request,user)
               return redirect('Home')
           else:
              return redirect("After_Login")
             
        
    return render(request,'Login.html')

def Sign_up(request):
    if request.method == "POST":
        Name = request.POST.get('Name')
        Email=request.POST.get('Email')
        Password = request.POST.get('Password')
        Address=request.POST.get('Address')
        City=request.POST.get('City')
        State=request.POST.get('State')
        Zip=request.POST.get('Zip')
        sign_up = SignUp(Name = Name ,Email=Email, Password=Password, Address=Address, City=City, State=State, Zip=Zip)
        sign_up.save()
        # return HttpResponse("User has been created Successfully")
        # return redirect("Login")
        sign_up = authenticate(request,Name=Name, Email=Email, Password= Password)
        if sign_up is not None:
            login(request, sign_up)
            return redirect('Home')
        else:
            return render(request, 'Sign_up.html', {'error': 'Invalid username or password'})
    return render(request,'Sign_up.html')

def Forget_password(request):
    return render(request,'Forget_password.html')

def Services(request):
    return render(request,'Services.html')

def Checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone, amount=amount)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        param_dict={

            'MID': 'Merchantid_2484',
            'ORDER_ID': 'order.order_id',
            'TXN_AMOUNT': '1',
            'CUST_ID': 'email',
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL':'http://127.0.0.1:8000/Checkout/',
        }
        return  render(request, 'Paytm.html', {'param_dict': param_dict})
    return render(request, 'Checkout.html')

@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'Paymentstatus.html', {'response': response_dict})


def Customer(request):
    if request.method == 'POST':
       Email = request.POST.get('Email')
       Comment = request.POST.get('Comment')
       customer = Customer_Support(Email=Email, Comment=Comment)
       customer.save()
       return HttpResponse("Thanks")
    return render(request, 'Customer.html')

def After_Login(request):
    return render(request,'After_Login.html')

# def Payment(request):
    return render(request,'Payment.html')

# def Checkout(request):
#     return render(request,'Checkout.html')

  
