# Generated by Django 5.1.1 on 2024-10-08 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_alter_maincategory_name_alter_subcategory_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
