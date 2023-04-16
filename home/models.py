"""
This module contains Django model classes for the User model, \
utilizing Django's built-in User model
and other related models for authentication and authorization purposes.
"""
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
    ("Other", "Other"),
    ("Salary", "Salary"),
    ("Business", "Business")
]
ADD_EXPENSE_CHOICES = [
    ("Expense", "Expense"),
    ("Income", "Income")
]
PROFESSION_CHOICES = [
    ("Employee", "Employee"),
    ("Business", "Business"),
    ("Student", "Student"),
    ("Other", "Other"),
    ("Salary", "Salary"),
    ("Business", "Business")
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
        """
        Meta class for configuring the database table name for the 'addmoney' model.
        """
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
    