# Generated by Django 5.0 on 2023-12-28 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Actor_name', models.CharField(max_length=50)),
                ('Actor_des', models.TextField()),
            ],
        ),
    ]
