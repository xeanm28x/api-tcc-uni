# Generated by Django 5.0.2 on 2024-04-19 21:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PedidoItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data_cadastro', models.DateTimeField(default=datetime.datetime.today)),
                ('data_atualizacao', models.DateTimeField(default=datetime.datetime.today)),
                ('quantidade', models.IntegerField()),
                ('comentario', models.CharField(max_length=128)),
            ],
        ),
    ]
