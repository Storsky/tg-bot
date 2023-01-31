# Generated by Django 4.1.5 on 2023-01-29 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Thread_Trigger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=100)),
                ('from_thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_thread', to='kites_game.thread')),
                ('to_thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_thread', to='kites_game.thread')),
            ],
        ),
        migrations.AddField(
            model_name='thread',
            name='trigger',
            field=models.ManyToManyField(through='kites_game.Thread_Trigger', to='kites_game.thread'),
        ),
    ]
