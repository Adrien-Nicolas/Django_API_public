from django.db import models

# Create your models here.
class User(models.Model):
    pseudo = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)
    UID = models.CharField(max_length=100)
    isAdmin = models.BooleanField(default=False)
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.UID


class Place(models.Model):
    name = models.CharField(max_length=60)
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    long = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    precision = models.FloatField()
    population = models.FloatField()
    quality = models.FloatField()
    def __str__(self):
        return self.name


class Opinion(models.Model):
    IDuser = models.ForeignKey(User, on_delete=models.CASCADE)
    IDplace = models.ForeignKey(Place, on_delete=models.CASCADE)
    rating = models.FloatField()
    comment = models.CharField(max_length=60)
    date = models.DateTimeField()
    def __str__(self):
        return self.comment


class User_Opinion(models.Model):
    IDuser = models.ForeignKey(User, on_delete=models.CASCADE)
    IDopinion = models.ForeignKey(Opinion, on_delete=models.CASCADE)
    def __str__(self):
        return self.IDuser.UID + " " + self.IDopinion.comment


class Place_Opinion(models.Model):
    IDplace = models.ForeignKey(Place, on_delete=models.CASCADE)
    IDopinion = models.ForeignKey(Opinion, on_delete=models.CASCADE)
    def __str__(self):
        return self.IDplace.name + " " + self.IDopinion.comment


class Presence(models.Model):
    IDuser = models.ForeignKey(User, on_delete=models.CASCADE)
    IDplace = models.ForeignKey(Place, on_delete=models.CASCADE)
    date = models.DateTimeField()
    timeStart = models.TimeField()
    timeEnd = models.TimeField()
    def __str__(self):
        return self.IDuser.UID + " " + self.IDplace.name
