# Generated by Django 5.1.6 on 2025-03-04 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='pradeep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('phone_number', models.IntegerField(unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
