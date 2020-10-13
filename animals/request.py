import sqlite3
import json
from sqlite3.dbapi2 import connect
from models import Animal

ANIMALS = [
    {
        "id": 1,
        "name": "Snickers",
        "species": "Dog",
        "locationId": 1,
        "customerId": 4,
        "status": "admitted"
    },
    {
        "id": 2,
        "name": "Gypsy",
        "species": "Dog",
        "locationId": 1,
        "customerId": 2,
        "status": "admitted"
    },
    {
        "id": 3,
        "name": "Blue",
        "species": "Cat",
        "locationId": 2,
        "customerId": 1,
        "status": "admitted"
    }
]


def get_all_animals():
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.customer_id,
            a.location_id
        FROM Animal a
        """)

        # Initialize an empty list to hold all animal representations
        animals = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            animal = Animal(row['id'], row['name'], row['breed'],
                            row['status'], row['location_id'],
                            row['customer_id'])

            animals.append(animal.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(animals)



# Function with a single parameter
def get_single_animal(id):
    with sqlite3.connect("./kennel.db") as connection:
        connection.row_factory = sqlite3.Row
        cursorObj = connection.cursor()
        
        cursorObj.execute("""
        SELECT 
            a.id,
            a.name,
            a.breed,
            a.status,
            a.customer_id,
            a.location_id
        FROM Animal a
        WHERE a.id = ?    
        """, ( id, ))

        foundSQLObj = cursorObj.fetchone()

        animalPythonObj = Animal(foundSQLObj['id'], foundSQLObj['name'], foundSQLObj['breed'], foundSQLObj['status'], foundSQLObj['location_id'],
        foundSQLObj['customer_id'])

        return json.dumps(animalPythonObj.__dict__)

def create_animal(animal):
    # Get the id value of the last animal in the list
    max_id = ANIMALS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    animal["id"] = new_id

    # Add the animal dictionary to the list
    ANIMALS.append(animal)

    # Return the dictionary with `id` property added
    return animal

def delete_animal(id):
    animal_index = -1
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            animal_index = index
    
    if animal_index >= 0:
        ANIMALS.pop(animal_index)

def update_animal(id, updated_animal):
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            ANIMALS[index] = updated_animal
            break
