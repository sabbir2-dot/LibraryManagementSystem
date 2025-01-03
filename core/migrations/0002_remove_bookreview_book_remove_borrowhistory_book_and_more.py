# Generated by Django 5.1.4 on 2024-12-29 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookreview',
            name='book',
        ),
        migrations.RemoveField(
            model_name='borrowhistory',
            name='book',
        ),
        migrations.RemoveField(
            model_name='bookreview',
            name='user',
        ),
        migrations.RemoveField(
            model_name='borrowhistory',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='BookReview',
        ),
        migrations.DeleteModel(
            name='BorrowHistory',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
