
from django.contrib import admin
from django.urls import path, include

#create a router for Expenses
from rest_framework.routers import DefaultRouter
from expenses.views import ExpenseViewSet
from expenses.views import home

router=DefaultRouter()
router.register('expenses', ExpenseViewSet)




urlpatterns = [
    #add api url
    path('', home), 
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]

admin.site.site_header = "Expense Calculator Admin"
