# Generated by Django 4.0.3 on 2022-05-06 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_basetable_po'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basetable',
            name='BC',
        ),
        migrations.RemoveField(
            model_name='basetable',
            name='PMC',
        ),
        migrations.AddField(
            model_name='basetable',
            name='BC1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='basetable',
            name='BC2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='basetable',
            name='BC3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='basetable',
            name='BC4',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='basetable',
            name='PMC1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='basetable',
            name='PMC2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='basetable',
            name='PMC3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='basetable',
            name='PMC4',
            field=models.BooleanField(default=False),
        ),
    ]
