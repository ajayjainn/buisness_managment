from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Customer, Transaction
from django.contrib import messages
from datetime import datetime,timedelta
from django.db.models import Sum

def home(request):
    name = request.GET.get('name','')
    customers = Customer.objects.filter(name__icontains=name).order_by('name')
    return render(request, 'index.html', context={'customers':customers})

def account(request,id):
    customer = Customer.objects.get(id=id)
    return render(request,'account.html',context={'customer':customer})

def update(request, id):
    customer = Customer.objects.get(id=id)
    remarks = request.POST.get('remarks')
    amount = request.POST.get('amount')
    tea = request.POST.get('tea')

    if tea=='' and amount=='' and remarks=='':
        messages.error(request,'All fields cannot be empty.')
        return redirect(request.META.get('HTTP_REFERER', '/'))

    if amount=='': amount=0
    else: amount = int(amount)

    if tea == '':tea=0
    else: tea=float(tea)

    
    closingBalance = customer.amountPending + (tea*300-amount)

    Transaction.objects.create(customer=customer, remarks=remarks, amount=amount, tea=tea,
    closingBalance=closingBalance).save()

    customer.amountPending = closingBalance
    customer.save()

    messages.success(request,"Transaction successful! ")
    return redirect(request.META.get('HTTP_REFERER', '/'))

def newCustomer(request):
    return render(request,'newCustomer.html')

def saveCustomer(request):
    customer_name = request.POST.get('name')
    if not customer_name:
        messages.error(request,'Enter customer name!')
        return redirect('newCustomer')
    phone_num = request.POST.get('number')
    amount = request.POST.get('amount')
    if amount == '':
        amount = 0

    Customer.objects.create(name=customer_name,amountPending=amount, phoneNo=phone_num).save()
    messages.success(request,"Successfully added.")
    return redirect('newCustomer')

def data(request):
    debtors = Customer.objects.order_by('-amountPending')[:3]

    # Last 30 days transactions
    one_month = datetime.today() - timedelta(days=30)
    data30 = Transaction.objects.filter(date__gte=one_month).aggregate(collection=Sum('amount'),tea_sold=Sum('tea'))

    # Last 1 day's transactions (Today)
    data1 = Transaction.objects.filter(date=datetime.today()).aggregate(collection=Sum('amount'),tea_sold=Sum('tea'))

    totalcredit = Customer.objects.aggregate(total=Sum('amountPending'))['total']

    context = {
        'data30':data30,
        'data1':data1,
        'debtors':debtors,
        'totalcredit':totalcredit
    }
    return render(request,'data.html',context=context)
    