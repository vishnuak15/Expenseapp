from django.db import models
from django.urls import reverse
from datetime import datetime    
from django.contrib.auth.models import User
from django.db.models import Sum
# Create your models here.
#  title 
#  status
#  date - current 
#  user 
#  priority

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Expense(models.Model):
    owner  = models.ForeignKey(User  , on_delete= models.CASCADE)
    description = models.CharField(max_length=50)
    category = models.ForeignKey(Category,  on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    detials = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.description
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})
    
    
    