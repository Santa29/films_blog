# Generated by Django 3.1.1 on 2020-09-25 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FilmReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film_name', models.CharField(max_length=256)),
                ('actors', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ReviewComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_comment', models.CharField(max_length=250)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
