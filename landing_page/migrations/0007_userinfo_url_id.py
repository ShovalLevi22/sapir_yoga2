# Generated by Django 3.0.3 on 2020-04-11 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0006_remove_userinfo_url_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='url_id',
            field=models.CharField(default='', max_length=7),
        ),
    ]