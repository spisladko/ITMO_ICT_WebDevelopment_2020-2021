# Generated by Django 3.1.2 on 2020-10-11 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0007_auto_20201010_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownership',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.car'),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.person'),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='end',
            field=models.DateField(default='1970-01-01'),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='start',
            field=models.DateField(default='1970-01-01'),
        ),
    ]
