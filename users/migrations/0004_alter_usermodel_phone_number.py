# Generated by Django 4.1.3 on 2022-11-28 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_usermodel_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
