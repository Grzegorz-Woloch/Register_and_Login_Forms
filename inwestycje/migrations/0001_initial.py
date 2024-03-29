# Generated by Django 3.0 on 2019-12-11 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=164)),
                ('description', models.TextField()),
                ('profitability', models.FloatField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('files', models.FileField(default='settings.MEDIA_ROOT/media/random_photo.png', upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=164)),
                ('product', models.ManyToManyField(to='inwestycje.Product')),
            ],
        ),
    ]
