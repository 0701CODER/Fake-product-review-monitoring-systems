# Generated by Django 4.0.4 on 2022-05-04 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_review_text_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='review_pred',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]