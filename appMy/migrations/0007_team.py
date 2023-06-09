# Generated by Django 4.1.3 on 2023-05-04 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0006_detailcard'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_img', models.ImageField(upload_to='images/', verbose_name='profil fotoğrafı')),
                ('team_name', models.CharField(max_length=50, verbose_name='ad/soyad')),
                ('team_comment', models.TextField(verbose_name='')),
            ],
        ),
    ]
