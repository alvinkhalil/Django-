# Generated by Django 3.2.5 on 2021-07-15 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20210715_1426'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_authpr',
            new_name='comment_author',
        ),
    ]