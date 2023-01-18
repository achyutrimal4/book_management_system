# Generated by Django 4.1.3 on 2023-01-18 02:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=250)),
                ('purchase_date', models.DateField(verbose_name='Date of Purchase')),
                ('isbn', models.CharField(max_length=250)),
                ('price', models.FloatField(verbose_name='Price')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
