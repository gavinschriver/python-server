import sqlite3
import json
from models import Customer

conObj = sqlite3.connect("./kennel.db")
rowFact = sqlite3.Row

def get_all_customers():
    with conObj as conn:
      conn.row_factory = sqlite3.Row
      dbcursor = conn.cursor()
      dbcursor.execute("""
        SELECT
          c.id,
          c.name,
          c.address,
          c.email,
          c.password
        FROM Customer AS c
      """)
      allCustomers = []
      for pythonTuple in dbcursor.fetchall():
        allCustomers.append(Customer(pythonTuple['id'], pythonTuple['name'], pythonTuple['address'], pythonTuple['email'], pythonTuple['password']).__dict__)
      return json.dumps(allCustomers)

def get_single_customer(id):
    with sqlite3.connect("./kennel.db") as connection:
      connection.row_factory = sqlite3.Row
      db_cursor = connection.cursor()
      db_cursor.execute("""
      SELECT
        c.id,
        c.name,
        c.address,
        c.email,
        c.password
      FROM Customer c
      WHERE c.id = ?
      """, (id, ))
      foundCust = db_cursor.fetchone()
      return json.dumps(Customer(foundCust['id'], foundCust['name'], foundCust['address'], foundCust['email'], foundCust['password']).__dict__)

def get_customers_by_email(emailValue):
    with sqlite3.connect("./kennel.db") as connection:
      connection.row_factory = sqlite3.Row
      db_cursor = connection.cursor()
      db_cursor.execute("""
        SELECT
          c.id,
          c.name,
          c.address,
          c.email,
          c.password
        FROM Customer as C
        WHERE c.email = ?    
      """, ( emailValue, ))
      customerList = []
      data = db_cursor.fetchall()
      for row in data:
        customer = Customer(row['id'], row['name'], row['address'], row['email'], row['password'])
        customerList.append(customer.__dict__)
    return json.dumps(customerList)