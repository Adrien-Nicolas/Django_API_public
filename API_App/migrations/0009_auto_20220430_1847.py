# Generated by Django 3.2.5 on 2022-04-30 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API_App', '0008_auto_20220430_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opinion',
            name='comment',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='acces_handicape',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='acces_juridique',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='acces_public',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='acces_secours',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='actif',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='adresse',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='adresse_internet',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='adresse_proprio',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='alerte',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='annee_mise_service',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='artmaj',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='atlas',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='cdc',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='civilite_personne_ressource',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='code2016',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='code_dept',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='code_reg',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='codeinsee',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='codepostal',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='codetypequipement',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='com',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='commune',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='commune_proprio',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='courriel_proprio',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='cp_proprio',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='date_creation',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='debit_horaire_maximal',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='douches',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='eclairage',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='equipement_acces_libre',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='famille',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='fonction_personne_ressource',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='installation_gardiennee',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='installation_multicommunes',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='mail_personne_ressource',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='nature_equipement',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='nature_sol',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='nb_vestiaires',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='ncc',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='nom_dept',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='nom_du_batiment',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='nom_gestionnaire',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='nom_personne_ressource',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='nom_proprio',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='nom_region',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='nomequipement',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='nominstallation',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='numequipement',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='numinstallation',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='ouverture_saison',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='phone_personne_ressource',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='phone_proprio',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='prenom_personne_ressource',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='prenom_proprio',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='restauration',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='sanitaires',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='surface_aire',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='tagequipement',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='tncc',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='type_utilisateur',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='type_utilisation',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='spot',
            name='typequipement',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='UID',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='pseudo',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
