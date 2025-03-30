from django.contrib import admin
from .models import Expense, Category, Statement

admin.site.register(Category)


@admin.register(Statement)
class StatementAdmin(admin.ModelAdmin):
    
    """
    Adds the user who is creating it as the user who is the owner
    of the statement.
    """
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_filter = ("date", "statement", "category")
    search_fields = ("description", )
    list_display = ("date", "description", "amount", "currency", "category")

    ordering = ("date",)
