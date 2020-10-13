from employees.request import delete_employee
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import urllib

from employees import get_all_employees, get_single_employee, create_employee, delete_employee, get_employee_by_location
from locations import get_all_locations, get_single_location, create_location, delete_location
from animals import get_all_animals, get_single_animal, delete_animal, create_animal, update_animal, get_animals_by_location, get_animals_by_status
from customers import get_all_customers, get_customers_by_email, get_single_customer

HANDLERS = {
    "animals": {
        "get_all": get_all_animals,
        "get_single": get_single_animal,
        "get_by_location": get_animals_by_location,
        "get_by_status": get_animals_by_status,
        "create": create_animal,
        "delete": delete_animal,
        "update": update_animal
    },
    "locations": {
        "get_all": get_all_locations,
        "get_single": get_single_location,
        "create": create_location,
        "delete": delete_location
    },
    "employees": {
        "get_all": get_all_employees,
        "get_single": get_single_employee,
        "get_by_location": get_employee_by_location,
        "create": create_employee,
        "delete": delete_employee
    },
    "customers": {
        "get_all": get_all_customers,
        "get_single": get_single_customer,
        "get_by_email": get_customers_by_email
    }
}

class HandleRequests(BaseHTTPRequestHandler):
    def parse_url(self, path):
        path_params = path.split("/")
        resource = path_params[1]
        if "?" in resource:
            resource, param = resource.split("?")
            key, value = param.split("=")
            value = urllib.parse.unquote(value)
            return (resource, key, value)

        else:   
            id = None
            try:
                id = int(path_params[2])
            except IndexError:
                pass  
            except ValueError:
                pass  
            return (resource, id) 


    # Here's a class function
    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    # Here's a method on the class that overrides the parent's method.
    def do_GET(self):
        self._set_headers(200)
        response = {} 

        parsed = self.parse_url(self.path)
        # if `parsed` tuple is 2 entries long, it's either a request for whole collection or 1 thing by id
        if len(parsed) == 2:
            (resourceName, id) = parsed
            handlerDict = HANDLERS[resourceName]
            if id is not None:
                response = f"{handlerDict['get_single'](id)}"
            else: 
                response = f"{handlerDict['get_all']()}" 

        elif len(parsed) == 3:
            (resourceName, key, value) = parsed
            handlerDict = HANDLERS[resourceName]
            if key == "email":
                response = f"{handlerDict['get_by_email'](value)}"
            if key == "location_id":
                response = f"{handlerDict['get_by_location'](value)}"
            if key == "status":
                response = f"{handlerDict['get_by_status'](value)}"

        self.wfile.write(response.encode())        
    # Here's a method on the class that overrides the parent's method.
    # It handles any POST request.
    def do_POST(self):
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Initialize new resource
        resource_creation_handler = HANDLERS[resource]['create']
        new_resource = resource_creation_handler(post_body)

        self.wfile.write(f"{new_resource}".encode())

    # Here's a method on the class that overrides the parent's method.
    # It handles any PUT request.
    def do_PUT(self):
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)
        (resource, id) = self.parse_url(self.path)
        resource_update_handler = HANDLERS[resource]["update"]
        resource_update_handler(id, post_body)
        self.wfile.write("".encode())

    def do_DELETE(self):
        self._set_headers(204)
        (resource, id) = self.parse_url(self.path)

        delete_handler = HANDLERS[resource]["delete"]
        delete_handler(id)
        self.wfile.write("".encode())


# This function is not inside the class. It is the starting
# point of this application.
def main():
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()

if __name__ == "__main__":
    main()