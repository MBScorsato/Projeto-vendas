# Generated by Django 4.2.11 on 2024-04-14 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bootstrap_navbar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_navbar', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Nome site',
            },
        ),
    ]
