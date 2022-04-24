#!/bin/bash

DB_FILE=db.sqlite3
ENV_FOLDER=env/

rm -f $DB_FILE

if [[ ! -d "$ENV_FOLDER" ]]
then
    python -m venv $ENV_FOLDER
fi

source $ENV_FOLDER/Scritps/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

python manage.py migrate


