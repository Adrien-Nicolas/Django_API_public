from django.contrib.gis.db import models

# Create your models here.
class User(models.Model):
    pseudo = models.CharField(null=True,max_length=200)
    password = models.CharField(null=True,max_length=200)
    email = models.EmailField(null=True,max_length=200)
    UID = models.CharField(null=True,max_length=500)
    isAdmin = models.BooleanField(default=False)
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.UID

    def save(self, *args, **kwargs):
        print(self.id)
        if self.id:
            print('updating')
        else:
            print('creating')
        super(User, self).save(*args, **kwargs)


class Place(models.Model):
    name = models.CharField(null=True,max_length=200)
    latitude=models.DecimalField(null=True, max_digits=10, decimal_places=7)
    longitude=models.DecimalField(null=True, max_digits=10, decimal_places=7)
    precision = models.FloatField()
    population = models.FloatField()
    quality = models.FloatField()
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.id:
            print('updating')
        else:
            print('creating')
        super(Place, self).save(*args, **kwargs)


class Opinion(models.Model):
    IDuser = models.ForeignKey(User, on_delete=models.CASCADE)
    IDplace = models.ForeignKey(Place, on_delete=models.CASCADE)
    rating = models.FloatField()
    comment = models.CharField(null=True,max_length=200)
    date = models.DateTimeField()
    def __str__(self):
        return self.comment

    def save(self, *args, **kwargs):
        if self.id:
            print('updating')
        else:
            print('creating')
        super(Opinion, self).save(*args, **kwargs)


class User_Opinion(models.Model):
    IDuser = models.ForeignKey(User, on_delete=models.CASCADE)
    IDopinion = models.ForeignKey(Opinion, on_delete=models.CASCADE)
    def __str__(self):
        return self.IDuser.UID + " " + self.IDopinion.comment

    def save(self, *args, **kwargs):
        if self.id:
            print('updating')
        else:
            print('creating')
        super(User_Opinion, self).save(*args, **kwargs)


class Place_Opinion(models.Model):
    IDplace = models.ForeignKey(Place, on_delete=models.CASCADE)
    IDopinion = models.ForeignKey(Opinion, on_delete=models.CASCADE)
    def __str__(self):
        return self.IDplace.name + " " + self.IDopinion.comment

    def save(self, *args, **kwargs):
        if self.id:
            print('updating')
        else:
            print('creating')
        super(Place_Opinion, self).save(*args, **kwargs)


class Presence(models.Model):
    IDuser = models.ForeignKey(User, on_delete=models.CASCADE)
    IDplace = models.ForeignKey(Place, on_delete=models.CASCADE)
    date = models.DateField()
    timeStart = models.TimeField()
    timeEnd = models.TimeField()
    def __str__(self):
        return self.IDuser.UID + " " + self.IDplace.name
    
    def save(self, *args, **kwargs):
        if self.id:
            print('updating')
        else:
            print('creating')
        super(Presence, self).save(*args, **kwargs)


class Spot(models.Model):
    numinstallation = models.CharField(null=True,max_length=200)
    nominstallation = models.CharField(null=True,max_length=200)
    adresse = models.CharField(null=True,max_length=500)
    codepostal = models.CharField(null=True,max_length=500)
    commune = models.CharField(null=True,max_length=500)
    codeinsee = models.CharField(null=True,max_length=11)
    actif = models.CharField(null=True,max_length=500)
    date_creation = models.DateField(null=True)
    acces_handicape = models.CharField(null=True,max_length=500)
    installation_gardiennee = models.CharField(null=True,max_length=500)
    installation_multicommunes = models.CharField(null=True,max_length=500)
    restauration = models.CharField(null=True,max_length=500)
    nb_equipements = models.IntegerField(null=True)
    nb_places_parking = models.IntegerField(null=True)
    nb_places_parking_handicap = models.IntegerField(null=True)
    numequipement = models.CharField(null=True,max_length=14)
    nomequipement = models.CharField(null=True,max_length=500)
    codetypequipement = models.CharField(null=True,max_length=500)
    typequipement = models.CharField(null=True,max_length=500)
    famille = models.CharField(null=True,max_length=500)
    tagequipement = models.CharField(null=True,max_length=500)
    coordgpsx =   models.DecimalField(null=True, max_digits=10, decimal_places=7)
    coordgpsy =  models.DecimalField(null=True, max_digits=10, decimal_places=7)
    eclairage = models.CharField(null=True,max_length=500)
    equipement_acces_libre = models.CharField(null=True,max_length=500)
    nb_vestiaires = models.IntegerField(null=True)
    ouverture_saison = models.CharField(null=True,max_length=500)
    douches = models.CharField(null=True,max_length=500)
    sanitaires = models.CharField(null=True,max_length=500)
    alerte = models.CharField(null=True,max_length=500)
    ERP_cat = models.IntegerField(null=True)
    hauteur_aire = models.IntegerField(null=True)
    largeur_aire = models.IntegerField(null=True)
    longueur_aire = models.IntegerField(null=True)
    surface_aire = models.CharField(null=True,max_length=500)
    places_tribune = models.IntegerField(null=True)
    debit_horaire_maximal = models.CharField(null=True,max_length=10)
    nom_du_batiment = models.CharField(null=True,max_length=500)
    adresse_internet = models.CharField(null=True,max_length=500)
    annee_mise_service = models.CharField(null=True,max_length=4)
    prenom_personne_ressource = models.CharField(null=True,max_length=500)
    nom_personne_ressource = models.CharField(null=True,max_length=500)
    mail_personne_ressource = models.CharField(null=True,max_length=500)
    phone_personne_ressource = models.CharField(null=True,max_length=500)
    fonction_personne_ressource = models.CharField(null=True,max_length=500)
    civilite_personne_ressource = models.CharField(null=True,max_length=500)
    nom_proprio = models.CharField(null=True,max_length=500)
    prenom_proprio = models.CharField(null=True,max_length=500)
    adresse_proprio = models.CharField(null=True,max_length=500)
    cp_proprio = models.CharField(null=True,max_length=500)
    commune_proprio = models.CharField(null=True,max_length=500)
    phone_proprio = models.CharField(null=True,max_length=500)
    courriel_proprio = models.CharField(null=True,max_length=500)
    nom_gestionnaire = models.CharField(null=True,max_length=500)
    type_utilisation = models.CharField(null=True,max_length=500)
    type_utilisateur = models.CharField(null=True,max_length=500)
    acces_public = models.CharField(null=True,max_length=500)
    acces_secours = models.CharField(null=True,max_length=500)
    nature_sol = models.CharField(null=True,max_length=500)
    nature_equipement = models.CharField(null=True,max_length=500)
    acces_juridique = models.CharField(null=True,max_length=500)
    atlas = models.CharField(null=True,max_length=500)
    cdc = models.CharField(null=True,max_length=500)
    artmaj = models.CharField(null=True,max_length=500)
    nom_region = models.CharField(null=True,max_length=500)
    tncc = models.CharField(null=True,max_length=500)
    ncc = models.CharField(null=True,max_length=500)
    com = models.CharField(null=True,max_length=500)
    code2016 = models.CharField(null=True,max_length=500)
    code_dept = models.CharField(null=True,max_length=500)
    nom_dept = models.CharField(null=True,max_length=500)
    code_reg = models.CharField(null=True,max_length=500)
    point_coord_spot = models.PointField(null=True, srid=4326)
    
    def __str__(self):
        return self.nomequipement
    
    def save(self, *args, **kwargs):
        if self.id:
            print('updating')
        else:
            print('creating')
        super(Spot, self).save(*args, **kwargs)


