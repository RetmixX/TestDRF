# Generated by Django 4.1.7 on 2023-03-11 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_customuser_is_superuser_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]