# Generated by Django 4.0.4 on 2022-06-01 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_account_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='location',
            field=models.TextField(blank=True, null=True),
        ),
    ]
