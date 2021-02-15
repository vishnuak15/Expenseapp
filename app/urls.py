
from django.contrib import admin
from django.urls import path
from . import views
from app.views import home , login , signup , signout 
import app.api_views


urlpatterns = [
   path('' , home , name='home' ), 
   path('login/' ,login  , name='login'), 
   path('signup/' , signup, name='register' ), 
   path('logout/' , signout , name='logout'), 
   path('entry/', views.Entry, name='entry'),
    #path('<id>/delete', delete_view,name='delete'), 
   path('dashboard/', views.Dashboard, name='dashboard'),
   path('list/', views.List, name='list'),
   path('<int:pk>/', views.detail, name='detail'), 
   path('delete/<int:pk>/',views.delete, name='delete'),
   path('update/<int:pk>/',views.update, name='update'),
   path('api/v1/Expense/',app.api_views.ExpenseList.as_view()),
   path('api/v1/Expense/new',app.api_views.ExpenseCreate.as_view()),
   path('api/v1/Expense/<int:id>',app.api_views.ExpenseRetrieveUpdateDestroyAPIView.as_view()),
]
