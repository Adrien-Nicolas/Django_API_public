# Django_API_public

Make with 
[![My Skills](https://skills.thijs.gg/icons?i=python,django,)](https://skills.thijs.gg)

### Objectives

*This API aims to return and list all sports parks in France. 

*It is only the hidden part of the iceberg, as it is only half of a project called SportDehors 
(an application allowing a user to search for a sport park nearby).

### Features

The API can be requested to obtain the following data:

  *Sports parks (objects, coordinates, properties) according to their id
  *Sports parks (objects, coordinates, properties) according to their equipment types
  *Sports parks where their point coordinates are in a specified polygon (by entering 2 point coordinates in 2d)
  *The user profiles of the application
  *Comments from users of the application

```json
{
    "Points": [
        {
            "coordinates": [
                1.07627,
                44.63226
            ],
            "properties": {
                "spot_point_id": 21503
            },
            "type": "Spot_Point",
            "type_equipement": "Terrain de pétanque"
        },
        {
            "coordinates": [
                1.07752,
                44.63223
            ],
            "properties": {
                "spot_point_id": 21504
            },
            "type": "Spot_Point",
            "type_equipement": "Bassin ludique de natation"
        }
    ]
}

```

### Configurations and use 

Before run, you must install library of projects :

```
pip install requirements.txt
```

Then Django's library are installed, you could run django project in local with 
```
python manage.py runserver
```

Because The api are not finished yet, You must have a PostgreSQL database, and change settings in API_SPOT/settings/prod.py

You could populate your database whith an intern command of this project :

```
python manage.py populate_spot
```
You could find this command in API_APP/management/commands/populate_spot.py
