# Generated by Django 5.0.6 on 2024-05-22 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_converter_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streamingcontent',
            name='country',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='streamingcontent',
            name='date_added',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='streamingcontent',
            name='description',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='streamingcontent',
            name='director',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='streamingcontent',
            name='duration',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='streamingcontent',
            name='rating',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='streamingcontent',
            name='title',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='streamingcontent',
            name='type',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
