# Generated by Django 4.2.5 on 2023-10-17 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0003_accesorio_imagen_url_zapato_imagen_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='userregistro',
            name='password',
            field=models.CharField(default=2, max_length=8),
            preserve_default=False,
        ),
    ]