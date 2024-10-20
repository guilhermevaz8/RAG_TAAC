# Generated by Django 5.1 on 2024-10-17 09:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0005_chaterror'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chatmessage',
            options={'ordering': ['created_at']},
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='response_rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='contextselection',
            name='KS_parameters',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='contextselection',
            name='VS_parameters',
            field=models.TextField(blank=True),
        ),
        migrations.CreateModel(
            name='OriginalScores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('origin', models.CharField(max_length=100)),
                ('selection_instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='original_scores', to='chatapp.selecteddocuments')),
            ],
        ),
    ]