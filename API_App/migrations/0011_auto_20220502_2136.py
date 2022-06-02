# Generated by Django 3.2.5 on 2022-05-02 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API_App', '0010_auto_20220502_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spot',
            name='acces_secours',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='adresse_internet',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='adresse_proprio',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='artmaj',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='atlas',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='cdc',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='code2016',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='code_dept',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='code_reg',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='com',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='commune_proprio',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='courriel_proprio',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='famille',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='fonction_personne_ressource',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='mail_personne_ressource',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='nature_equipement',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='nature_sol',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='ncc',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='nom_dept',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='nom_du_batiment',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='nom_gestionnaire',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='nom_personne_ressource',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='nom_proprio',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='nom_region',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='prenom_proprio',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='tncc',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='type_utilisateur',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='type_utilisation',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='typequipement',
            field=models.CharField(max_length=100, null=True),
        ),
    ]