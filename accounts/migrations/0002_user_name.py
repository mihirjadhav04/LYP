# Generated by Django 4.0.3 on 2022-05-10 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='Saurabh Ghadge', max_length=100),
            preserve_default=False,
        ),
    ]
