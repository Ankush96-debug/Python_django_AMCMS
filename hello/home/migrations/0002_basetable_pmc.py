# Generated by Django 4.0.3 on 2022-03-26 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basetable',
            name='PMC',
            field=models.CharField(default='NA', max_length=5),
        ),
    ]