# Generated by Django 4.1.3 on 2023-05-04 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0009_company_company_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_head',
            field=models.CharField(max_length=100, null=True, verbose_name='Başlık'),
        ),
    ]
