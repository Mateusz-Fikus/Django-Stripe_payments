# Generated by Django 3.2 on 2021-04-20 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('desc', models.TextField()),
                ('price', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('image', models.ImageField(upload_to='product_pictures')),
            ],
        ),
    ]
