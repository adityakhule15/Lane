# Generated by Django 4.0.5 on 2022-12-28 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.DecimalField(decimal_places=0, max_digits=100)),
                ('dislike', models.DecimalField(decimal_places=0, max_digits=100)),
            ],
            options={
                'db_table': 'count',
            },
        ),
    ]