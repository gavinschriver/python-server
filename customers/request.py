CUSTOMERS = [
    {
      "id": 1,
      "name": "Hannah Hall",
      "address": "7002 Chestnut Ct"
    },
    {
      "id": 2,
      "name": "James Schroeder",
      "address": "14 Ellington Street"
    },
    {
      "id": 3,
      "name": "Jenny Penny",
      "address": "1-2 Menny"
    },
    {
      "email": "ITSYABOIITHO@YABOII.YA",
      "password": "yaboy",
      "name": "NOT YA MOM NOT YA DADDY",
      "id": 4
    },
    {
      "email": "fuckkkshit@gmail.fuck",
      "password": "fuck",
      "name": "Another person Goddamnit",
      "id": 5
    },
    {
      "email": "whydoyou@whydoyou.suck",
      "password": "yousuck",
      "name": "BLEH NAW",
      "id": 6
    },
    {
      "email": "myface@myface.myface",
      "password": "myface",
      "name": "myface myface",
      "id": 7
    },
    {
      "email": "nah@nah.nah",
      "password": "nah",
      "name": "nah nah",
      "id": 8
    },
    {
      "email": "nah@nah.nah",
      "password": "nah",
      "name": "nah nah",
      "id": 9
    },
    {
      "email": "gavy@gavy.gavy",
      "password": "gavy",
      "name": "gavy gavy",
      "id": 10
    },
    {
      "email": "fuck@fuck.fuck",
      "password": "fuck",
      "name": "fuck fuck",
      "id": 11
    }
]

def get_all_customers():
    return CUSTOMERS

def get_single_customer(id):
    requested_customer = None

    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer
    
    return requested_customer