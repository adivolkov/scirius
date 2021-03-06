# Generated by Django 2.2.13 on 2020-06-24 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suricata', '0004_auto_20160316_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suricata',
            name='created_date',
            field=models.DateTimeField(verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='suricata',
            name='output_directory',
            field=models.CharField(max_length=400, verbose_name='Rules directory'),
        ),
        migrations.AlterField(
            model_name='suricata',
            name='updated_date',
            field=models.DateTimeField(blank=True, verbose_name='date updated'),
        ),
        migrations.AlterField(
            model_name='suricata',
            name='yaml_file',
            field=models.CharField(max_length=400, verbose_name='Suricata configuration file'),
        ),
    ]
