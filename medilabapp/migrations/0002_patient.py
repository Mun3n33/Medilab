# Generated by Django 5.0.6 on 2024-07-05 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medilabapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('Emailaddress', models.EmailField(max_length=200)),
                ('medicalhistory', models.TextField()),
                ('age', models.IntegerField()),
            ],
        ),
    ]
