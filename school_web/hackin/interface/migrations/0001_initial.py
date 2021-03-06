# Generated by Django 2.2 on 2020-07-01 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adm_no', models.IntegerField()),
                ('first_name', models.TextField(max_length=20)),
                ('last_name', models.TextField(max_length=20)),
                ('subject', models.TextField(max_length=20)),
                ('working_days', models.IntegerField()),
                ('present_days', models.IntegerField()),
                ('half_days', models.IntegerField()),
                ('absent_days', models.IntegerField()),
            ],
        ),
    ]
