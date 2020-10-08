EMPLOYEES = [
    {
      "id": 1,
      "name": "Jerry",
      "locationId": 2
    },
    {
      "id": 2,
      "name": "Jeremi",
      "locationId": 1
    },
    {
      "id": 3,
      "name": "Jeremiah",
      "locationId": 1
    },
    {
      "name": "yikee",
      "locationId": 1,
      "id": 6
    },
    {
      "name": "Big oll shitpants",
      "locationId": 2,
      "id": 7
    },
    {
      "name": "trying",
      "locationId": 1,
      "id": 8
    },
    {
      "name": "dontmatta",
      "locationId": 1,
      "id": 9
    },
    {
      "name": "YA DADDYEE",
      "locationId": 2,
      "id": 11
    }
]

def get_all_employees():
    return EMPLOYEES

def get_single_employee(id):
    requested_employee = None

    for employee in EMPLOYEES:

        if employee["id"] == id:
            requested_employee = employee

    return requested_employee

def create_employee(employee):
    max_id = EMPLOYEES[-1]["id"]
    new_id = max_id + 1
    employee["id"] = new_id
    EMPLOYEES.append(employee)
    return employee

def delete_employee(id):
    employee_index = -1
    for index, employee in enumerate(EMPLOYEES):
      if employee["id"] == id:
        employee_index = index
    
    if employee_index >= 0:
      EMPLOYEES.pop(employee_index)




