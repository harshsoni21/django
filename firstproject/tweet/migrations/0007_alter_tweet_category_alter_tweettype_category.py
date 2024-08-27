# Generated by Django 5.1 on 2024-08-24 07:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0006_alter_tweet_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='category',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='tweet.tweettype'),
        ),
        migrations.AlterField(
            model_name='tweettype',
            name='category',
            field=models.CharField(choices=[('ENT', 'Entertainment'), ('SPT', 'Sports'), ('NEW', 'News'), ('TECH', 'Technology'), ('OTH', 'Other')], default='OTH', max_length=4),
        ),
    ]
