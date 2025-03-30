from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Statement, Expense, Category

@receiver(post_save, sender=Statement)
def create_expenses_after_statement_save(sender, instance, created, **kwargs):
    if created and instance.parsed_json:
        for item in instance.parsed_json:
            category = Category.objects.get_or_create(name=item['category'])[0]
            Expense.objects.create(
                amount=item['amount'],
                description=item['description'],
                description_raw=item['description_raw'],
                currency=item['currency'],
                date=item['date'],
                category_id=category.pk,
                user_id=instance.user.pk,
                statement_id=instance.pk,
            )
