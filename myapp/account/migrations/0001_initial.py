# Generated by Django 4.0.4 on 2022-06-01 11:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('mobile_no', models.BigIntegerField()),
                ('email', models.EmailField(max_length=255)),
                ('age', models.IntegerField()),
                ('address', models.TextField()),
                ('hobbies', models.CharField(max_length=255)),
                ('workout_preferences', models.TextField()),
                ('dietary_preferences', models.TextField()),
                ('gender', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE'), ('OTH', 'OTHERS')], max_length=6)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
