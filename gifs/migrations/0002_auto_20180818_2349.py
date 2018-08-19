# Generated by Django 2.1 on 2018-08-19 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gif',
            name='contador',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='gif',
            name='descripcion',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='gif',
            name='url',
            field=models.TextField(default='#'),
        ),
        migrations.AlterField(
            model_name='gif',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
