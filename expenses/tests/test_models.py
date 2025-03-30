from django.test import TestCase
from django.contrib.auth.models import User
from expenses.models import Category, Statement, Expense
from decimal import Decimal


class ExpenseModelTest(TestCase):

    def test_category_created(self):
        Category.objects.create(
            name="Food",
            description="This category will store the expenses related to food.",
            description_for_parser="food"
        )

        category = Category.objects.get(name="Food")
        self.assertEqual(category.name, "Food")
        self.assertEqual(
            category.description, "This category will store the expenses related to food.")
        self.assertEqual(category.description_for_parser, "food")


class StatementModelSignalsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.category = Category.objects.create(name='General')

    def test_create_expense_on_statement_save(self):
        data = [
            {
                'amount': '100.00',
                'description': 'Groceries purchase',
                'currency': 'USD',
                'category': self.category.id,
                'user': self.user.id
            },
            {
                'amount': '200.00',
                'description': 'Rent payment',
                'currency': 'ARS',
                'category': self.category.id,
                'user': self.user.id
            },
        ]

        statement = Statement.objects.create(
            title="Test Statement",
            statement_type="DEBIT",
            billing_cycle_date="2023-01-01",
            parsed_json=data
        )

        self.assertEqual(Expense.objects.count(), 2)

        expense1, expense2 = Expense.objects.all().order_by('id')
        self.assertEqual(expense1.amount, Decimal('100.00'))
        self.assertEqual(expense1.description, 'Groceries purchase')
        self.assertEqual(expense1.currency, 'USD')
        self.assertEqual(expense1.category, self.category)
        self.assertEqual(expense1.user, self.user)

        self.assertEqual(expense2.amount, Decimal('200.00'))
        self.assertEqual(expense2.description, 'Rent payment')
        self.assertEqual(expense2.currency, 'ARS')
        self.assertEqual(expense2.category, self.category)
        self.assertEqual(expense2.user, self.user)
