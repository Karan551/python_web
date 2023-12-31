# Generated by Django 4.2.4 on 2023-11-28 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('serial_number', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=250)),
                ('user_email', models.CharField(max_length=100)),
                ('user_phoneNumber', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=500)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
