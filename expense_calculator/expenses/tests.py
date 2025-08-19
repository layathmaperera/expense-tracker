# #imports for django_rest_framework tests
# from rest_framework.test import APITestCase

# from expenses.models import Expense
# """

# # Create your models here.
# class Expense(models.Model):
    
#     name= models.CharField(max_length=100)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     #category choice field
#     CATEGORY_CHOICES = [
#         ('Food', 'Food'),
#         ('Transport', 'Transport'),
#         ('Entertainment', 'Entertainment'),
#         ('Other', 'Other'),
#     ]
#     category = models.CharField(max_length=100,choices=CATEGORY_CHOICES)

#     def __str__(self):
#         return f"{self.name} - {self.amount}"


# """



# class ExpenseAPITestCase(APITestCase):
#     def setUp(self):
#         #creare 3 expenses
#         Expense.objects.bulk_create([
#             Expense(name='Food', amount=12.50, category='Food'),
#             Expense(name='Transport', amount=2.75, category='Transport'),
#             Expense(name='Entertainment', amount=15.00, category='Entertainment')
#         ])

#     def test_expense_list(self):
#         response = self.client.get('/expenses/')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(len(response.data), 3)

#     def test_expense_create(self):
#         response = self.client.post('/expenses/', {
#             'name': 'New Expense',
#             'amount': 20.00,
#             'category': 'Other'
#         },format='json')
#         self.assertEqual(response.status_code, 201)
#         self.assertEqual(response.json()['name'], 'Food')
#         self.assertEqual(response.json()['amount'], '12.50')
#         self.assertEqual(response.json()['category'], 'Food')

#     def test_expense_detail(self):
#         response = self.client.get('/expenses/1/')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json()['name'], 'Food')
#         self.assertEqual(response.json()['amount'], '12.50')
#         self.assertEqual(response.json()['category'], 'Food') 


#     def test_expense_update(self):
#         response = self.client.put('/api/expenses/1/', {
#             'name': 'Updated Expense',
#             'amount': 30.00,
#             'category': 'Transport'
#         })
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json()['name'], 'Updated Expense')
#         self.assertEqual(response.json()['amount'], '30.00')
#         self.assertEqual(response.json()['category'], 'Transport')

#     def test_expense_delete(self):
#         response = self.client.delete('/api/expenses/1/')
#         self.assertEqual(response.status_code, 204)
#         self.assertEqual(Expense.objects.count(), 2)
#     # Clean up after tests
#         self.assertEqual(Expense.objects.get(pk=1).name,'Transport')
#         self.assertEqual(Expense.objects.get(pk=2).name, 'Entertainment')
#         self.assertEqual(Expense.objects.get(pk=3).name, None)
#         self.assertEqual(Expense.objects.get(pk=3).amount, None)
#         self.assertEqual(Expense.objects.get(pk=3).category, None)
#         self.assertEqual(Expense.objects.get(pk=3).timestamp, None)


#         def tearDown(self):
#             Expense.objects.all().delete()  



from rest_framework.test import APITestCase
from django.urls import reverse
from expenses.models import Expense

class ExpenseAPITestCase(APITestCase):

    def setUp(self):
        Expense.objects.bulk_create([
            Expense(name='Food', amount=12.50, category='Food'),
            Expense(name='Transport', amount=2.75, category='Transport'),
            Expense(name='Entertainment', amount=15.00, category='Entertainment')
        ])

    def test_expense_list(self):
        url = reverse('expense-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)

    def test_expense_create(self):
        url = reverse('expense-list')
        data = {'name': 'New Expense', 'amount': 20.00, 'category': 'Other'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], 'New Expense')
        self.assertEqual(str(response.data['amount']), '20.00')
        self.assertEqual(response.data['category'], 'Other')

    def test_expense_detail(self):
        url = reverse('expense-detail', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Food')

    def test_expense_update(self):
        url = reverse('expense-detail', args=[1])
        data = {'name': 'Updated Expense', 'amount': 30.00, 'category': 'Transport'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Updated Expense')

    def test_expense_delete(self):
        url = reverse('expense-detail', args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Expense.objects.count(), 2)

    def tearDown(self):
        Expense.objects.all().delete()
