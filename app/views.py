from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate , login as loginUser , logout
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import (get_object_or_404, 
                              render,  
                              HttpResponseRedirect) 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from . forms import ExpenseForm
from django.shortcuts import render
from django.contrib import messages
from .models import Category,Expense
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView
from django.db.models import Sum
from django import template
from django.template.defaultfilters import stringfilter


#@login_required(login_url='login')

def login(request):
   
    if request.method == 'GET':
        # import pdb ; pdb.set_trace()
            
        form1 = AuthenticationForm()
        context = {
            'form' : form1
        }
        return render(request , 'login.html' , context=context )

    else:
        form = AuthenticationForm(data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username , password = password)
            if user is not None:
                loginUser(request , user)
                return redirect('dashboard')
            else:
                return redirect('signup')
        else:
            #context = {
            #    'form' : form}
            
            return render(request,'login.html' )


def signup(request):

    if request.method == 'GET':
        form = UserCreationForm()
        context = {
            "form" : form
        }
        return render(request , 'signup.html' , context=context)
    else:
        print(request.POST)
        form = UserCreationForm(request.POST)  
        context = {
            "form" : form
        }
        if form.is_valid():
            user = form.save()
            print(user)
            if user is not None:
                return redirect('login')
        else:
            return render(request , 'signup.html' , context=context)



#@login_required(login_url='login')


def signout(request):
    logout(request)
    return redirect('login')


 
def Entry(request): 
    context ={} 
    form = ExpenseForm(request.POST) 
    if form.is_valid(): 
        Expense = form.save(commit=False)
        Expense.owner = request.user 
        Expense.save()
        return redirect('list')
          
    context['form']= form 
    return render(request, "Entry.html", context) 


def delete(request, pk):
    program = get_object_or_404(Expense, pk=pk)
    program.delete()
    return redirect('list')


def detail(request, pk): 
    context ={} 
  
    context["data"] = Expense.objects.get(pk = pk) 
          
    return render(request, "detail.html", context) 


def update(request, pk): 
    context ={} 
  
    obj = get_object_or_404(Expense, pk = pk) 
    form = ExpenseForm(request.POST, instance = obj) 
  
    if form.is_valid(): 
        form.save() 
        Expense.owner = request.user 
        return redirect('detail', pk)
    
  
    context["form"] = form 
  
    return render(request, "update.html", context)  

def home(request):
    return render(request,'home.html',{})

def index(request):
    return render(request,'index.html',{})


def Dashboard(request):
    expenses = Expense.objects.filter(owner=request.user)  
    total = Expense.objects.filter(owner=request.user,category = 2).aggregate(Sum('amount'))
    TIncome = Expense.objects.filter(owner=request.user,category = 1).aggregate(Sum('amount'))
    #balance = None
    #balance = { 'amount__sum': TIncome['amount__sum'] - total['amount__sum'] }
        

    context = {
        'expenses':expenses,
        'total':total,
        'TIncome':TIncome,
        
    
        }
    return render(request,'dashboard.html',context )



def List(request):
    categories = Category.objects.all()
    entity_list = Expense.objects.filter(owner=request.user)  
    context = {
        'entity':entity_list
        }
    return render(request,'list.html',context )
