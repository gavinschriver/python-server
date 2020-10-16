import sqlite3
import json
from sqlite3.dbapi2 import connect
from models import Animal, Location, Customer

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
            a.location_id,
            l.name location_name,
            l.address location_address,
            c.name customer_name,
            c.address as customer_address
        FROM Animal a
        JOIN Location l ON l.id = a.location_id
        JOIN Customer c ON c.id = a.customer_id
        """)

        # Initialize an empty list to hold all animal representations
        animals = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            animal = Animal(row['id'], row['name'], row['breed'],
                            row['status'], row['location_id'],
                            row['customer_id'])
            location = Location(row['location_id'], row['location_name'], row['location_address'])
            customer = Customer(row['customer_id'], row['customer_name'], row['customer_address'])
            animal.location = location.__dict__
            animal.customer = customer.__dict__
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
            a.location_id,
            a.customer_id,
            l.name location_name,
            l.address location_address,
            c.name customer_name,
            c.address customer_address
        FROM Animal a
        JOIN Location l ON l.id = a.location_id
        JOIN Customer c ON c.id = a.customer_id 
        WHERE a.id = ?
        """, ( id, ))

        row = cursorObj.fetchone()
        animal = Animal(row['id'], row['name'], row['breed'], row['status'], row['location_id'],
        row['customer_id'])
        location = Location(row['location_id'], row['location_name'], row['location_address'])
        customer = Customer(row['customer_id'], row['customer_name'], row['customer_address'])
        animal.location = location.__dict__
        animal.customer = customer.__dict__
        return json.dumps(animal.__dict__)

def get_animals_by_location(loc):
    with sqlite3.connect("./kennel.db") as con:
        con.row_factory = sqlite3.Row
        cursor = con.cursor()
        cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.customer_id,
            a.location_id
        FROM Animal AS a
        WHERE a.location_id = ?    
        """, (loc,))
        list = []
        data = cursor.fetchall()
        print(data)
        for row in data:
            list.append(Animal(row['id'], row['name'], row['breed'], row['status'], row['location_id'], row['customer_id']).__dict__)
        return json.dumps(list)

def get_animals_by_status(status):
    with sqlite3.connect("./kennel.db") as con:
        con.row_factory = sqlite3.Row
        cursor = con.cursor()
        cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.customer_id,
            a.location_id
        FROM Animal AS a
        WHERE a.status = ?    
        """, (status,))
        list = []
        data = cursor.fetchall()
        print(data)
        for row in data:
            list.append(Animal(row['id'], row['name'], row['breed'], row['status'], row['location_id'], row['customer_id']).__dict__)
        return json.dumps(list)

def delete_animal(id):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        DELETE FROM Animal
        WHERE id = ?    
        """, (id, ))
        rows_affected = db_cursor.rowcount
        if rows_affected > 0:
            return True
        else:
            return False
            


def update_animal(id, updated_animal):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory= sqlite3.Row
        c = conn.cursor()
        c.execute("""
        UPDATE Animal
            SET 
                name = ?,
                breed = ?,
                status = ?,
                location_id = ?,
                customer_id = ?
        WHERE id = ?        
        """, (updated_animal['name'], updated_animal['breed'], updated_animal['status'], updated_animal['location_id'], updated_animal['customer_id'], id, ))
        if c.rowcount == 0:
            return False
        else:
            return True

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
