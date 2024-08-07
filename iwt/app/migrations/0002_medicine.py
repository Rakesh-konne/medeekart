# Generated by Django 4.2.3 on 2023-07-09 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Medicine",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=30)),
                (
                    "disease",
                    models.CharField(
                        choices=[
                            ("Cough", "Cough"),
                            ("Fever", "Fever"),
                            ("Skin Care", "Skin Care"),
                            ("Fitness and Wellness", "Fitness and Wellness"),
                            ("Baby Care", "Baby Care"),
                            ("Diabetis", "Diabetis"),
                        ],
                        max_length=30,
                    ),
                ),
                ("description", models.CharField(max_length=1000)),
                ("dosage", models.CharField(max_length=500)),
                ("price", models.CharField(default="Rs. 200", max_length=500)),
                ("image", models.URLField()),
            ],
        ),
    ]
