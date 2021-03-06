# Generated by Django 3.2 on 2021-04-10 15:52

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('header', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images/')),
                ('uploaded_date', models.DateField(default=datetime.datetime(2021, 4, 10, 16, 52, 30, 158933))),
            ],
        ),
    ]
