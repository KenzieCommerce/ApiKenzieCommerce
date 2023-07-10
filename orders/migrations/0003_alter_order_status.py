# Generated by Django 4.2.2 on 2023-07-10 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('EM ANDAMENTO', 'Andamento'), ('REALIZADO', 'Realizado'), ('ENTREGUE', 'Entregue')], default='REALIZADO', max_length=20),
        ),
    ]