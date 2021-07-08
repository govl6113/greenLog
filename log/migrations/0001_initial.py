# Generated by Django 3.2 on 2021-07-08 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plogging',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=10)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to=None)),
                ('date', models.DateTimeField()),
                ('firstPlace', models.CharField(max_length=30)),
                ('like', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kinds', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=10)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to=None)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=10)),
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('nickname', models.CharField(max_length=10)),
                ('profile', models.ImageField(upload_to=None)),
            ],
        ),
    ]
