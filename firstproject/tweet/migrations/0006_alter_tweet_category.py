# Generated by Django 5.1 on 2024-08-24 06:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0005_tweet_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='category',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='tweet.tweettype'),
        ),
    ]