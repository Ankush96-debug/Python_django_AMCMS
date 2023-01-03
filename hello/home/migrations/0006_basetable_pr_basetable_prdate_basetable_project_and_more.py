# Generated by Django 4.0.3 on 2022-04-07 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_basetable_po'),
    ]

    operations = [
        migrations.AddField(
            model_name='basetable',
            name='PR',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='basetable',
            name='PRdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='basetable',
            name='Project',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='basetable',
            name='oldPO',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='basetable',
            name='price',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='basetable',
            name='typePO',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='basetable',
            name='vendor',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
