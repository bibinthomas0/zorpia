# Generated by Django 4.2.7 on 2023-12-21 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_room_userslist'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room',
            field=models.ManyToManyField(blank=True, to='api.user'),
        ),
    ]
