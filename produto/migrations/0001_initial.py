# Generated by Django 5.0.4 on 2024-04-17 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=50)),
                ('valor_unitario', models.FloatField()),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
    ]
