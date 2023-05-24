from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse , HttpResponseRedirect
from .models import *
from datetime import datetime
from django.db.models import Sum



# Create your views here.
def home(request):
    user_id = request.user.id
    if request.method == 'POST':
        information = request.POST.get('information')
        amount = request.POST.get('amount')
        type = request.POST.get('type')
        print(user_id,information,amount,type)

        model = Data(user = request.user)
        model.info = information
        model.date_time = datetime.now()
        model.amount = amount
        model.type=type
        model.save()


    if request.user.is_authenticated:
        data = Data.objects.filter(user=request.user)
        debit = Data.objects.filter(user=request.user, type="debit").aggregate(total_amount=Sum('amount'))['total_amount']
        credit = Data.objects.filter(user=request.user , type = "credit").aggregate(total_amount=Sum('amount'))['total_amount']
        data = data.order_by('-date_time')[:15]
        context={
            "data" : data,
            "total_credit" : credit,
            "total_debit" : debit,
            }
        return render(request, 'index.html' , context=context)
            
    context={
        }
    return render(request, 'index.html' , context=context)

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = username)

        if not user_obj.exists():
            messages.warning(request, 'Account not found ')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        user_obj = authenticate(username = username , password = password)
        if not user_obj:
            messages.warning(request, 'Invalid password ')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        login(request , user_obj)
        return redirect('/')

        
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    if not request.user.is_authenticated:
        return render(request ,'login.html')
    else:
        return redirect("home")


def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        user_obj = User.objects.filter(username = username)

        if user_obj.exists():
            messages.warning(request, 'Username already exists')
            return render(request , 'register.html' , context={
                "first_name":first_name,
                'last_name':last_name,
                'email':email,
            })
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        user = User.objects.create(username = username)
        user.set_password(password)
        user.first_name=first_name
        user.last_name=last_name
        user.email=email
        user.save()

        return redirect('/')

    return render(request , 'register.html')

def logout_page(request):
    logout(request)
    return redirect("home")
    