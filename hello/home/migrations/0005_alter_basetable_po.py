# Generated by Django 4.0.3 on 2022-03-29 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_basetable_pmc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basetable',
            name='PO',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
