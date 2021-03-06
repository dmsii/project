# Generated by Django 2.2.5 on 2019-09-25 18:56

import apps.mockup.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('portfolio', '0002_auto_20190925_1752'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mockup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=apps.mockup.models.Mockup.lorem_default, max_length=200, null=True)),
                ('alt', models.CharField(default=apps.mockup.models.Mockup.lorem_default, max_length=400, null=True)),
                ('image', models.ImageField(null=True, upload_to='portfolio/img/')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mockups', to='portfolio.Portfolio')),
            ],
        ),
    ]
