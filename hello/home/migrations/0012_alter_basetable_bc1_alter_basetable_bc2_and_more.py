# Generated by Django 4.0.3 on 2022-05-06 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_remove_basetable_bc_remove_basetable_pmc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basetable',
            name='BC1',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='basetable',
            name='BC2',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='basetable',
            name='BC3',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='basetable',
            name='BC4',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='basetable',
            name='PMC1',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='basetable',
            name='PMC2',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='basetable',
            name='PMC3',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='basetable',
            name='PMC4',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
