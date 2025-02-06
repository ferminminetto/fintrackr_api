from django.test import TestCase
from expenses.models import Category


class ExpenseModelTest(TestCase):
    
    def test_category_created(self):
        Category.objects.create(
            name="Food",
            description="This category will store the expenses related to food.",
            description_for_parser="food"
        )

        category = Category.objects.get(name="Food")
        self.assertEqual(category.name, "Food")
        self.assertEqual(category.description, "This category will store the expenses related to food.")
        self.assertEqual(category.description_for_parser, "food")
