# Generated by Django 4.1.3 on 2023-05-04 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='welcome',
            name='text_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Fotoğraf yükle'),
        ),
    ]