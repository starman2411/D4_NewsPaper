# Generated by Django 4.1.1 on 2022-10-06 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_rename_username_author_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(blank=True, through='news.PostCategory', to='news.category'),
        ),
    ]
