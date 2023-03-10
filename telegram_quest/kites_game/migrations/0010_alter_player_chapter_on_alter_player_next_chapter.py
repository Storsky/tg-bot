# Generated by Django 4.1.5 on 2023-01-31 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kites_game', '0009_thread_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='chapter_on',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='player_recent', to='kites_game.thread'),
        ),
        migrations.AlterField(
            model_name='player',
            name='next_chapter',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='player_next', to='kites_game.thread'),
        ),
    ]
