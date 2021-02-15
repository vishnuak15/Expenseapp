from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView,GenericAPIView
#from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.exceptions import ValidationError

from app.serializers import ExpenseSerializer
from app.models import Expense,Category
from rest_framework import viewsets


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class ExpensePagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100


# class ExpenseList(ListAPIView):
#     queryset = Expense.objects.all()
#     serializer_class = ExpenseSerializer
#     pagination_class = ExpensePagination
   
# class ExpenseCreate(CreateAPIView):
#     serializer_class = ExpenseSerializer
    
#     def create(self,request,*args,**kwargs):
#         try:
#             amount = request.data.get('amount')
#             if amount is not None and float(amount) <= 0.0:
#                 raise ValidationError({ 'amount': 'Must be above $0.00' })
#         except ValueError:
#             raise ValidationError({'amount': 'A valid number is required'})
#         return super().create(request,*args,**kwargs)
    

# class ExpenseRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Expense.objects.all()
#     lookup_field = 'id'
#     serializer_class = ExpenseSerializer

#     def delete(self, request, *args, **kwargs):
#         product_id = request.data.get('id')
#         response = super().delete(request, *args, **kwargs)
#         if response.status_code == 204:
#             from django.core.cache import cache
#             cache.delete('product_data_{}'.format(product_id))
#         return response

#     def update(self, request, *args, **kwargs):
#         response = super().update(request, *args, **kwargs)
#         if response.status_code == 200:
#             from django.core.cache import cache
#             expense = response.data
#             cache.set('product_data_{}'.format(expense['id']),
#                       {
#                           'description':expense['description'],
#                           'category': expense['category'],
#                           'amount':expense['amount'],
#                           'detials':expense['detials'],
#                           'owner':expense['owner'],
#                       })
#         return response
  