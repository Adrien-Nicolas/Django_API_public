from itertools import count
import requests
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point


from API_App.models import Spot

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
    
        f_request = "https://equipements.sports.gouv.fr/api/records/1.0/search/?dataset=data-es&rows=10000&start=0"
        response = requests.get(f_request)
        file_json = response.json()
        for i in range (0, len(file_json["records"])):
            records_fields = file_json["records"][i]["fields"]
            point_spot_coord = Point(records_fields.get('coordgpsx'), records_fields.get('coordgpsy'))
            spot=Spot(
                numinstallation=records_fields.get('numinstallation'),
                nominstallation=records_fields.get('nominstallation'),
                adresse = records_fields.get('adresse'),
                codepostal = records_fields.get('codepostal'),
                commune = records_fields.get('commune'),
                codeinsee = records_fields.get('codeinsee'),
                actif = records_fields.get('actif'),
                date_creation = records_fields.get('date_creation'),
                acces_handicape = records_fields.get('caract3'),
                installation_gardiennee = records_fields.get('caract5'),
                installation_multicommunes = records_fields.get('caract8'),
                restauration = records_fields.get('caract9'),
                nb_equipements = records_fields.get('caract10'),
                nb_places_parking = records_fields.get('caract12'),
                nb_places_parking_handicap = records_fields.get('caract13'),
                numequipement = records_fields.get('numequipement'),
                nomequipement = records_fields.get('nomequipement'),
                codetypequipement = records_fields.get('codetypequipement'),
                typequipement = records_fields.get('typequipement'),
                famille = records_fields.get('famille'),    
                tagequipement = records_fields.get('tagequipement'),
                coordgpsx = records_fields.get('coordgpsx'),
                coordgpsy = records_fields.get('coordgpsy'),
                eclairage = records_fields.get('caract24'),
                equipement_acces_libre = records_fields.get('caract25'),
                nb_vestiaires = records_fields.get('caract74'),
                ouverture_saison = records_fields.get('caract33'),
                douches = records_fields.get('caract34'),
                sanitaires = records_fields.get('caract35'),
                alerte = records_fields.get('caract40'),
                ERP_cat = records_fields.get('caract66'),
                hauteur_aire = records_fields.get('caract67'),
                largeur_aire = records_fields.get('caract68'),
                longueur_aire = records_fields.get('caract69'),
                surface_aire = records_fields.get('caract70'),
                places_tribune = records_fields.get('caract72'),
                debit_horaire_maximal = records_fields.get('caract111'),
                nom_du_batiment = records_fields.get('caract116'),
                adresse_internet = records_fields.get('caract117'),
                annee_mise_service = records_fields.get('caract118'),
                prenom_personne_ressource = records_fields.get('caract119'),
                nom_personne_ressource = records_fields.get('caract120'),
                mail_personne_ressource = records_fields.get('caract121'),
                phone_personne_ressource = records_fields.get('caract122'),
                fonction_personne_ressource = records_fields.get('caract165'),
                civilite_personne_ressource = records_fields.get('caract166'),
                nom_proprio = records_fields.get('caract123'),
                prenom_proprio = records_fields.get('caract124'),
                adresse_proprio = records_fields.get('caract125'),
                cp_proprio = records_fields.get('caract126'),
                commune_proprio = records_fields.get('caract127'),
                phone_proprio = records_fields.get('caract128'),
                courriel_proprio = records_fields.get('caract130'),
                nom_gestionnaire = records_fields.get('caract139'),
                type_utilisation = records_fields.get('caract155'),
                type_utilisateur = records_fields.get('caract159'),
                acces_public = records_fields.get('caract161'),
                acces_secours = records_fields.get('caract162'),
                nature_sol = records_fields.get('caract167'),
                nature_equipement = records_fields.get('caract168'),
                acces_juridique = records_fields.get('caract180'),
                atlas = records_fields.get('atlas'),
                cdc = records_fields.get('cdc'),
                artmaj = records_fields.get('artmaj'),
                nom_region = records_fields.get('nom_region'),
                tncc = records_fields.get('tncc'),
                ncc = records_fields.get('ncc'),
                com = records_fields.get('com'),
                code2016 = records_fields.get('code2016'),
                code_dept = records_fields.get('code_dept'),
                nom_dept = records_fields.get('nom_dept'),
                code_reg = records_fields.get('code_reg'),
                point_coord_spot = point_spot_coord,
            )  
            spot.save()
            
