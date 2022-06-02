from itertools import count
import requests
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
   
        f_request = "https://equipements.sports.gouv.fr/api/records/1.0/search/?dataset=data-es&q=&facet=famille&facet=caract24&facet=caract25&facet=caract74&facet=caract33&facet=caract156&facet=caract159&facet=caract167&facet=caract168&facet=caract169&facet=atlas&facet=nom_region&facet=nom_dept&refine.famille=Terrain+ext%C3%A9rieur+de+petits+jeux+collectifs&codetypequipement=1701"
        s_request = "https://equipements.sports.gouv.fr/api/records/1.0/search/?dataset=data-es&q=City-Stade&refine.caract25=true"
        count_equipement = 0
        response = requests.get(s_request)
        file_json = response.json()
        print(file_json.keys())    
        print(len(file_json['records']))
        for i in range (0, len(file_json['records'])):
            print(file_json["records"][i]["fields"]["coordonnees"])
            print(file_json["records"][i]["fields"]["nomequipement"])
            print(file_json["records"][i]["fields"]["codetypequipement"])
            if (file_json["records"][i]["fields"]["codetypequipement"] == "1701"):
                count_equipement += 1 
            
        print(count_equipement)
     
                

    
      
