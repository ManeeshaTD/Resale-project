# Generated by Django 4.0 on 2023-05-01 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_rename_product_user_chatmessages_message_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
