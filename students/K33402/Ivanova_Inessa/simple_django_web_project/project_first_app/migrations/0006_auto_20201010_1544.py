# Generated by Django 3.1.2 on 2020-10-10 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0005_auto_20201010_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownership',
            name='car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project_first_app.car'),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='driver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project_first_app.person'),
        ),
    ]