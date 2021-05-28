# Generated by Django 3.2.3 on 2021-05-28 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=52, unique=True, verbose_name='Name')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]