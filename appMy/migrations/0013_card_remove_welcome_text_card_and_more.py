# Generated by Django 4.1.3 on 2023-05-04 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0012_rename_text_img_welcome_text_card_img_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_head', models.CharField(max_length=50, verbose_name='Başlık')),
                ('text', models.TextField(verbose_name='Alt yazı')),
            ],
        ),
        migrations.RemoveField(
            model_name='welcome',
            name='text_card',
        ),
        migrations.RemoveField(
            model_name='welcome',
            name='text_head',
        ),
    ]