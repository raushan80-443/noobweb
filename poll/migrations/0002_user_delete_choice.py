# Generated by Django 4.0.4 on 2022-06-13 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('number', models.IntegerField(max_length=10)),
                ('gender', models.CharField(max_length=10)),
                ('additonal_number', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]
