# Generated by Django 4.0.6 on 2022-07-12 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='image/avatar')),
                ('start_date', models.DateField(auto_now_add=True)),
                ('end_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]