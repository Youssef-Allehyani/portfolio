# Generated by Django 3.1.1 on 2021-02-13 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='works/static/img/')),
                ('titlle', models.CharField(max_length=100)),
                ('details', models.TextField()),
            ],
        ),
    ]
