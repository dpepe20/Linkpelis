# Generated by Django 2.1 on 2018-09-13 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pelis', '0003_auto_20180911_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='descarga',
            name='descripcion',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pelicula',
            name='trailer',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]