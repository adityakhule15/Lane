# Generated by Django 4.0.5 on 2022-12-28 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('count', '0002_alter_count_dislike_alter_count_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='count',
            name='pk1',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]