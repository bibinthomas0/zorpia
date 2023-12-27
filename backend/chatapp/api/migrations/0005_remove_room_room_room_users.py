# Generated by Django 4.2.7 on 2023-12-21 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_room_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='room',
        ),
        migrations.AddField(
            model_name='room',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='rooms', to='api.user'),
        ),
    ]
