# Generated by Django 3.2.5 on 2022-05-11 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API_App', '0018_rename_point_coord_point_spot_pointcoord'),
    ]

    operations = [
        migrations.RenameField(
            model_name='point_spot',
            old_name='pointCoord',
            new_name='point_coord_spot',
        ),
    ]
