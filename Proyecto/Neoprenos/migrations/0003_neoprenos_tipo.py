# Generated by Django 5.1.4 on 2024-12-12 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Neoprenos', '0002_cliente_pedido_sucursal'),
    ]

    operations = [
        migrations.AddField(
            model_name='neoprenos',
            name='tipo',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
