# Generated by Django 4.2 on 2024-11-16 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazins', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Revista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('slug', models.SlugField(editable=False, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Reviste',
            },
        ),
        migrations.AlterModelOptions(
            name='publicatie',
            options={'verbose_name_plural': 'Publicatii'},
        ),
    ]