# Generated by Django 4.1.5 on 2023-01-29 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kites_game', '0003_alter_thread_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='name',
            field=models.CharField(default='message', max_length=50, verbose_name='Наз'),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('chat_id', models.CharField(max_length=10)),
                ('chapter_on', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kites_game.thread')),
            ],
        ),
    ]
