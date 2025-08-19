from django.contrib import admin

# Register your models here.
from .models import Expense 

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
   
    list_display = ('name', 'amount', 'timestamp', 'category')
    list_filter = ('category', 'timestamp')
    search_fields = ('name', 'category__name')
















# from django.contrib import admin
# from .models import Expense, Category

# @admin.register(Expense)
# class ExpenseAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'amount', 'timestamp', 'category')
#     list_display_links = ('id', 'name', 'amount', 'timestamp', 'category')
#     list_filter = ('category', 'timestamp')
#     search_fields = ('name', 'amount', 'category__name')

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')
#     search_fields = ('name',)

 