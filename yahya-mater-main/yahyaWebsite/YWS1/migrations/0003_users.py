# Generated by Django 4.1.1 on 2022-10-11 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YWS1', '0002_alter_workers_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=64)),
                ('user_gmail', models.CharField(max_length=64)),
                ('user_password', models.CharField(max_length=64)),
            ],
        ),
    ]
