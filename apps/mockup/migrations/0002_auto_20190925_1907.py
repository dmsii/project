# Generated by Django 2.2.5 on 2019-09-25 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20190925_1752'),
        ('mockup', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mockup',
            options={'verbose_name': 'Mockup'},
        ),
        migrations.AddField(
            model_name='mockup',
            name='position',
            field=models.CharField(choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third')], default='First', max_length=20),
        ),
        migrations.AlterUniqueTogether(
            name='mockup',
            unique_together={('project', 'position')},
        ),
    ]
