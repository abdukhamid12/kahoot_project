# Generated by Django 5.0.7 on 2024-08-03 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kahoot_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_number',
            field=models.IntegerField(default=1),
        ),
    ]
