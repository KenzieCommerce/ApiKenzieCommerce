# Generated by Django 4.2.2 on 2023-07-03 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_initial'),
        ('users', '0002_user_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cart',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='carts.cart'),
        ),
    ]
