# Generated by Django 5.0.3 on 2024-04-13 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('type', models.CharField(max_length=100)),
                ('episodes', models.CharField(max_length=10)),
                ('status', models.CharField(choices=[('ONGOING', 'Ongoing'), ('FINISHED', 'finished'), ('UPCOMING', 'upcoming'), ('UNKNOWN', 'unknown')], max_length=80)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('season', models.CharField(max_length=80)),
                ('picture', models.CharField(max_length=100)),
                ('thumbnail', models.CharField(max_length=100)),
                ('relatedAnime', models.CharField(max_length=8000)),
                ('tags', models.ManyToManyField(blank=True, to='animeList.tag')),
            ],
        ),
    ]
