from rest_framework.viewsets import ModelViewSet
from .models import Expense
from .serializers import ExpenseSerializer

class ExpenseViewSet(ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    
from django.http import HttpResponse

def home(request):
    return HttpResponse("")  # returns a blank page
