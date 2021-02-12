from rest_framework import serializers

from .models import Unicorn

from .models import Category,Expense

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class ExpenseSerializer(serializers.ModelSerializer):
    MRP = serializers.FloatField(read_only=True)
    description = serializers.CharField(min_length=2, max_length=200)
    detials = serializers.CharField(min_length=5, max_length=200)
    
    class Meta:
        model = Expense
        fields = ('id',
            'description',
            'amount',
            'detials',
            'date' ,
            'owner',
            'category','MRP')

class UnicornSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Unicorn
        fields = ('name', 'age')
        
        