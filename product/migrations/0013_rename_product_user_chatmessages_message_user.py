# Generated by Django 4.0 on 2023-04-28 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_productchat_chatmessages'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chatmessages',
            old_name='product_user',
            new_name='message_user',
        ),
    ]
