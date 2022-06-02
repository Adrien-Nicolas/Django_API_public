from traceback import print_tb
import pandas as pd
from os.path import exists
from django.core.management.base import BaseCommand, CommandError
from API_App.models import User, Place, Opinion, User_Opinion, Place_Opinion, Presence

class Command(BaseCommand):
    help = "import dataset from csv file, with -f <folder>"

    def add_arguments(self, parser):
        parser.add_argument('-f', '--folder', type=str, help= "root folder to import all files")
    
    def import_from_folder(self, folder):
        try:
            self.stdout.write(self.style.SUCCESS("Importing from folder: " + folder))
            self.stdout.write(self.style.SUCCESS("Importing Users, from file: " + folder + "/User.csv"))
            print(folder + "/User.csv")
            self.import_users(folder + "/User.csv")
            self.stdout.write(self.style.SUCCESS("Importing Places, from file: " + folder + "/Place.csv"))
            self.import_places(folder + "/Place.csv")
            self.stdout.write(self.style.SUCCESS("Importing Opinions, from file: " + folder + "/Opinion.csv"))
            self.import_opinions(folder + "/Opinion.csv")
            self.stdout.write(self.style.SUCCESS("Importing User_Opinions, from file: " + folder + "/User_Opinion.csv"))
            self.import_user_opinions(folder + "/User_Opinion.csv")
            self.stdout.write(self.style.SUCCESS("Importing Place_Opinions from file: " + folder + "/Place_Opinion.csv"))
            self.import_place_opinions(folder + "/Place_Opinion.csv")
            self.stdout.write(self.style.SUCCESS("Importing Presences from file: " + folder + "/Presence.csv"))
            self.import_presences(folder + "/Presence.csv")
        except Exception as e:
            self.stdout.write(self.style.ERROR("Error: " + str(e)))
            print_tb(e.__traceback__)
    
    def import_users(self, file):
        df = pd.read_csv(file,sep = ';')
        
        for index, row in df.iterrows():
            print("here")
            user = User(
                id=row['ID'],
                pseudo=row['pseudo'],
                password=row['password'],
                email=row['email'],
                UID=row['UID'],
                isAdmin=row['isAdmin'],
                isDelete=row['isDelete']
            )
            user.save()
            # send to API
    
    def import_places(self, file):
        df = pd.read_csv(file,sep = ';')

        for index, row in df.iterrows():
            place = Place(
                id=row['ID'],
                name=row['name'],
                latitude=row['latitude'],
                longitude=row['longitude'],
                precision=row['precision'],
                population=row['population'],
                quality=row['quality']
            )
            place.save()

    def import_opinions(self, file):
        df = pd.read_csv(file,sep = ';', encoding='iso-8859-1')
        for index, row in df.iterrows():
            user = User.objects.get(id=row['Iduser'])
            place = Place.objects.get(id=row['IDplace'])
            opinion = Opinion(
                id=row['ID'],
                IDuser=user,
                IDplace=place,
                rating=row['rating'],
                comment=row['comment'],
                date=row['date']
            )
            opinion.save()
    
    def import_user_opinions(self, file):
        df = pd.read_csv(file,sep = ';')
        for index, row in df.iterrows():
            user=User.objects.get(id=row['IDuser'])
            opinion=Opinion.objects.get(id=row['IDopinion'])
            user_opinions = User_Opinion(
                id=row['ID'],
                IDuser=user,
                IDopinion=opinion
            )
            user_opinions.save()
    
    def import_place_opinions(self, file):
        df = pd.read_csv(file,sep = ';')
        for index, row in df.iterrows():
            place=Place.objects.get(id=row['IDplace'])
            opinion=Opinion.objects.get(id=row['IDopinion'])
            place_opinions = Place_Opinion(
                id=row['ID'],
                IDplace=place,
                IDopinion=opinion
            )
            place_opinions.save()
    
    def import_presences(self, file):
        df = pd.read_csv(file,sep = ';')
        for index, row in df.iterrows():
            user = User.objects.get(id=row['IDuser'])
            place = Place.objects.get(id=row['Idplace'])
            presence = Presence(
                id=row['ID'],
                IDuser=user,
                IDplace=place,
                date=row['date'],
                timeStart=row['timeStart'],
                timeEnd=row['timeEnd']
            )
            presence.save()

    def handle(self, *args, **options):
        try:
            if options['folder'] is None:
                raise CommandError("You must provide a folder directory to import, see --help")
            elif not exists(options['folder']):
                raise CommandError("Folder does not exist")
            else:
                self.stdout.write(self.style.SUCCESS("Importing from folder: " + options['folder']))
                self.import_from_folder(options['folder'])
        except Exception as e:
            self.stdout.write(self.style.ERROR("Error: " + str(e)))
            print_tb(e.__traceback__)