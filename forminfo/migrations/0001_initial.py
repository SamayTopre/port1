# Generated by Django 4.2.3 on 2023-09-15 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='forminfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('mail', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=200)),
            ],
        ),
    ]
