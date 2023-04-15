from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.

SELECT_CATEGORY_CHOICES = [
    ("Food", "Food"),
    ("Travel", "Travel"),
    ("Shopping", "Shopping"),
    ("Necessities", "Necessities"),
    ("Entertainment", "Entertainment"),
    ("Other", "Other")
]
ADD_EXPENSE_CHOICES = [
    ("Expense", "Expense"),
    ("Income", "Income")
]
PROFESSION_CHOICES = [
    ("Employee", "Employee"),
    ("Business", "Business"),
    ("Student", "Student"),
    ("Other", "Other")
]


class Addmoney_info(models.Model):
    """
    Model to store information about added money transactions.
    """
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    add_money = models.CharField(max_length=10, choices=ADD_EXPENSE_CHOICES)
    quantity = models.BigIntegerField()
    Date = models.DateField(default=now)
    Category = models.CharField(
        max_length=20, choices=SELECT_CATEGORY_CHOICES, default='Food')

    class Meta:
        db_table: 'addmoney'


class UserProfile(models.Model):
    """
    Model representing a user profile, associated with a User model via OneToOneField.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profession = models.CharField(max_length=10, choices=PROFESSION_CHOICES)
    Savings = models.IntegerField(null=True, blank=True)
    income = models.BigIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.user.username
