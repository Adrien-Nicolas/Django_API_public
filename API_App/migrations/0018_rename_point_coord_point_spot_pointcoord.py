# Generated by Django 3.2.5 on 2022-05-10 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API_App', '0017_point_spot'),
    ]

    operations = [
        migrations.RenameField(
            model_name='point_spot',
            old_name='point_coord',
            new_name='pointCoord',
        ),
    ]