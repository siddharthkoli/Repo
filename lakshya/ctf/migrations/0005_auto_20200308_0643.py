# Generated by Django 2.1.5 on 2020-03-08 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctf', '0004_auto_20200308_0553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='solved',
            field=models.IntegerField(default=0, null=True),
        ),
    ]