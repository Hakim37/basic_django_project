# Generated by Django 3.2.4 on 2021-06-25 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarSpecs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_brand', models.CharField(max_length=100)),
                ('car_engine', models.CharField(max_length=100)),
                ('production_year', models.IntegerField(max_length=10)),
            ],
        ),
    ]