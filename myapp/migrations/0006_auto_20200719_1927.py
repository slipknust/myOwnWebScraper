# Generated by Django 3.0.8 on 2020-07-19 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20200719_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='data_nasc',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='email',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
