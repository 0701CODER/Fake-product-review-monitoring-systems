# Generated by Django 3.2.13 on 2022-04-23 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('product_description', models.TextField()),
                ('product_price', models.IntegerField()),
                ('product_image', models.FileField(upload_to='product_images')),
            ],
        ),
    ]
