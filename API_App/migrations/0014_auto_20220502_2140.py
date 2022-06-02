# Generated by Django 3.2.5 on 2022-05-02 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API_App', '0013_rename_code20120_spot_code2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spot',
            name='acces_handicape',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='acces_juridique',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='acces_public',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='actif',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='alerte',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='civilite_personne_ressource',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='codepostal',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='codetypequipement',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='cp_proprio',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='douches',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='eclairage',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='equipement_acces_libre',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='installation_gardiennee',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='installation_multicommunes',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='ouverture_saison',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='phone_personne_ressource',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='phone_proprio',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='prenom_personne_ressource',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='restauration',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='sanitaires',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='surface_aire',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='tagequipement',
            field=models.CharField(max_length=100, null=True),
        ),
    ]