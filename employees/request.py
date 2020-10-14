from models.employee import Employee
import sqlite3
import json
from models import Location

def get_all_employees():
    with sqlite3.connect("./kennel.db") as con:
      con.row_factory = sqlite3.Row
      db_cursor = con.cursor()
      db_cursor.execute("""
      SELECT 
        e.id,
        e.name,
        e.address,
        e.location_id
      FROM Employee e  
      """)
      employeeList = []
      dataset = db_cursor.fetchall()
      for row in dataset:
        empObj = Employee(row['id'], row['name'], row['address'], row['location_id'], "")
        employeeList.append(empObj.__dict__)
      return json.dumps(employeeList)

def get_single_employee(id):
       with sqlite3.connect("./kennel.db") as con:
        con.row_factory = sqlite3.Row
        db_cursor = con.cursor()
        db_cursor.execute("""
        SELECT 
          e.id,
          e.name,
          e.address,
          e.location_id
        FROM Employee e  
        WHERE e.id = ?
        """, (id, ))

        empTuple = db_cursor.fetchone()
        empObj = Employee(empTuple['id'], empTuple['name'], empTuple['address'], empTuple['location_id'], "")
        return json.dumps(empObj.__dict__)  

def get_employee_by_location(loc):
        with sqlite3.connect("./kennel.db") as con:
          con.row_factory = sqlite3.Row
          db_cursor = con.cursor()
          db_cursor.execute("""
          SELECT 
            e.id,
            e.name,
            e.address,
            e.location_id
          FROM Employee e  
          WHERE e.location_id = ?
          """, (loc, ))
          list = []
          data = db_cursor.fetchall()
          for row in data:
            list.append(Employee(row['id'], row['name'], row['address'], row['location_id']).__dict__)
          return json.dumps(list)

def delete_employee(id):
  with sqlite3.connect("./kennel.db") as conn:
    cursor = conn.cursor()
    cursor.execute("""
    DELETE FROM Employee
    WHERE id = ?
    """, (id, )
    )
    if cursor.rowcount > 0:
      return True
    else:
      return False

def create_employee(employee):
    max_id = EMPLOYEES[-1]["id"]
    new_id = max_id + 1
    employee["id"] = new_id
    EMPLOYEES.append(employee)
    return employee




