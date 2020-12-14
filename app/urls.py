
from django.contrib import admin
from django.urls import path
from . import views
from app.views import home , login , signup , signout 


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
]
