# Generated by Django 4.0.3 on 2022-10-27 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_rename_city_user_liveplace'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='describe',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='user',
            name='not_twf_exp',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]
