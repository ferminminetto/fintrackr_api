from django.db import models
from common.BaseModel import BaseModel
from django.contrib.auth.models import User


"""
Category model will be used to store the different categories of expenses or incomes.
"""
class Category(BaseModel):

    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    """
    This will store the instructions for the AI tool to associate a certain expense description with the
    category name.
    """
    description_for_parser = models.TextField()

    def __str__(self):
        return self.name


"""
Statement model will be used to store the bank statements from a debit or credit card.
"""
class Statement(BaseModel):
    
    title = models.CharField(max_length=255)
    statement_type = models.CharField(
        choices=[('DEBIT', 'Debit'), ('CREDIT', 'credit')], max_length=10
    )
    file_name = models.CharField(max_length=255, null=True, blank=True)

    # The original JSON that will be parsed to extract the expenses and incomes (in the future).
    parsed_json = models.JSONField(null=True, blank=True)

    """
    This field will be used to store the date of the billing cycle.
    Example: If the billing cycle is from 1st to 30th of the month, this field will store the 1st of the month.
    """
    billing_cycle_date = models.DateField()
    description = models.CharField(max_length=255, null=True, blank=True)

    def store(self, statement_file):
        # This method will store the statement file in the database or S3 depending the implementation.
        # StatementRepository.store(statement_file)
        self.save()
        return self


"""
Expense model will be used to store the expenses or incomes.
"""
class Expense(BaseModel):

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    currency = models.CharField(max_length=3)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    statement = models.ForeignKey(Statement, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.amount} {self.currency} - {self.description}'