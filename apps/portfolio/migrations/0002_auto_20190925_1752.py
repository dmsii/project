# Generated by Django 2.2.5 on 2019-09-25 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='link',
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(null=True, upload_to='portfolio/img/'),
        ),
    ]
