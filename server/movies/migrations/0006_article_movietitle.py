# Generated by Django 3.2.3 on 2021-05-22 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='movietitle',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]