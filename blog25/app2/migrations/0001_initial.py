# Generated by Django 5.0 on 2024-01-05 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actoress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Actoress_name', models.CharField(max_length=50)),
                ('Actoress_des', models.TextField()),
            ],
        ),
    ]
