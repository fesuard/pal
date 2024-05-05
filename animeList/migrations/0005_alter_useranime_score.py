# Generated by Django 5.0.4 on 2024-05-05 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animeList', '0004_alter_useranime_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranime',
            name='score',
            field=models.IntegerField(blank=True, choices=[(1, '(1) Appalling'), (2, '(2) Horrible'), (3, '(3) Very Bad'), (4, '(4) Bad'), (5, '(5) Average'), (6, '(6) Fine'), (7, '(7) Good'), (8, '(8) Very Good'), (9, '(9) Great'), (10, '(10) Masterpiece')], null=True),
        ),
    ]
