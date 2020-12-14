from django.forms import ModelForm 
from .models import Category,Expense
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms 


class ExpenseForm(forms.ModelForm):

    class Meta:
        model = Expense 
        fields = ('description','category','amount','detials','date')
        
        widgets = {
            'description' : forms.TextInput(attrs={'class': 'form-control'}),
            'category' : forms.Select(attrs={'class': 'form-control'}),
            'amount' : forms.NumberInput(attrs={'class': 'form-control'}),
            'detials' : forms.Textarea(attrs={'class': 'form-control'}),
            'date' : forms.DateInput(attrs={'class':'form-control','type':'date'}),
            
        }