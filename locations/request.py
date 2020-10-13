import sqlite3
import json
from models import Location

def get_all_locations():
    with sqlite3.connect("./kennel.db") as con:
        con.row_factory = sqlite3.Row
        cursor = con.cursor()

        cursor.execute("""
        SELECT 
            l.id,
            l.name,
            l.address
        FROM Location l
        """)

        locations = []

        datacollection = cursor.fetchall()

        for tuple in datacollection:
            location = Location(tuple['id'], tuple['name'], tuple['address'])
        
            locations.append(location.__dict__)
    return json.dumps(locations)

def get_single_location(id):
    with sqlite3.connect("./kennel.db") as con:
        con.row_factory = sqlite3.Row
        cursor = con.cursor()
        cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address
        FROM Location l
        WHERE l.id = ?   
        """, (id, ))

        sqlResultAsPythonObject = cursor.fetchone()

        location = Location(sqlResultAsPythonObject['id'], sqlResultAsPythonObject['name'], sqlResultAsPythonObject['address'])

        return json.dumps(location.__dict__)


def create_location(location):
    max_id = LOCATIONS[-1]["id"]
    new_id = max_id + 1
    location["id"] = new_id
    LOCATIONS.append(location)
    return location

def delete_location(id):
    location_index = -1
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            location_index = index
    
    if location_index >0:
        LOCATIONS.pop(location_index)