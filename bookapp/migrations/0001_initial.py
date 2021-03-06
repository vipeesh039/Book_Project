# Generated by Django 3.2 on 2021-04-29 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=150, unique=True)),
                ('author', models.CharField(max_length=150)),
                ('price', models.IntegerField()),
                ('pages', models.IntegerField()),
            ],
        ),
    ]
