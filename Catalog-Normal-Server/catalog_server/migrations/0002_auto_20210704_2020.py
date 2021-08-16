# Generated by Django 3.2.4 on 2021-07-04 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_server', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='topic',
            field=models.CharField(max_length=80, null=True),
        ),
    ]