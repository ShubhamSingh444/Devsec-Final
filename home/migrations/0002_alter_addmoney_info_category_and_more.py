# Generated by Django 4.2 on 2023-04-16 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="addmoney_info",
            name="Category",
            field=models.CharField(
                choices=[
                    ("Food", "Food"),
                    ("Travel", "Travel"),
                    ("Shopping", "Shopping"),
                    ("Necessities", "Necessities"),
                    ("Entertainment", "Entertainment"),
                    ("Other", "Other"),
                    ("Salary", "Salary"),
                    ("Business", "Business"),
                ],
                default="Food",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="profession",
            field=models.CharField(
                choices=[
                    ("Employee", "Employee"),
                    ("Business", "Business"),
                    ("Student", "Student"),
                    ("Other", "Other"),
                    ("Salary", "Salary"),
                    ("Business", "Business"),
                ],
                max_length=10,
            ),
        ),
    ]
