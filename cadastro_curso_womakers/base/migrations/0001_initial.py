# Generated by Django 4.2.10 on 2024-03-08 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=75)),
                ('senha', models.CharField(max_length=50)),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
