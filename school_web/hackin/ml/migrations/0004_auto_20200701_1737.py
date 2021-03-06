# Generated by Django 2.2 on 2020-07-01 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ml', '0003_auto_20200701_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mod',
            name='activities',
            field=models.CharField(choices=[('no', 'NO'), ('yes', 'Yes')], max_length=10),
        ),
        migrations.AlterField(
            model_name='mod',
            name='famsup',
            field=models.CharField(choices=[('no', 'NO'), ('yes', 'Yes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='mod',
            name='higher',
            field=models.CharField(choices=[('no', 'NO'), ('yes', 'Yes')], max_length=10),
        ),
        migrations.AlterField(
            model_name='mod',
            name='internet',
            field=models.CharField(choices=[('no', 'NO'), ('yes', 'Yes')], max_length=10),
        ),
        migrations.AlterField(
            model_name='mod',
            name='nursery',
            field=models.CharField(choices=[('no', 'NO'), ('yes', 'Yes')], max_length=10),
        ),
        migrations.AlterField(
            model_name='mod',
            name='paid',
            field=models.CharField(choices=[('no', 'NO'), ('yes', 'Yes')], max_length=10),
        ),
        migrations.AlterField(
            model_name='mod',
            name='rom',
            field=models.CharField(choices=[('no', 'NO'), ('yes', 'Yes')], max_length=10),
        ),
        migrations.AlterField(
            model_name='mod',
            name='schoolsup',
            field=models.CharField(choices=[('no', 'NO'), ('yes', 'Yes')], max_length=3),
        ),
    ]
