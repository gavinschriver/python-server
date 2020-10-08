from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from employees import get_all_employees, get_single_employee, create_employee
from locations import get_all_locations, get_single_location, create_location
from animals import get_all_animals, get_single_animal, delete_animal, create_animal
from customers import get_all_customers, get_single_customer

HANDLERS = {
    "animals": {
        "get_all": get_all_animals,
        "get_single": get_single_animal,
        "create": create_animal,
        "delete": delete_animal
    },
    "locations": {
        "get_all": get_all_locations,
        "get_single": get_single_location,
        "create": create_location
    },
    "employees": {
        "get_all": get_all_employees,
        "get_single": get_single_employee,
        "create": create_employee
    },
    "customers": {
        "get_all": get_all_customers,
        "get_single": get_single_customer
    }
}


# Here's a class. It inherits from another class.
class HandleRequests(BaseHTTPRequestHandler):
    def parse_url(self, path):
        # Just like splitting a string in JavaScript. If the
        # path is "/animals/1", the resulting list will
        # have "" at index 0, "animals" at index 1, and "1"
        # at index 2.
        path_params = path.split("/")
        resource = path_params[1]
        id = None

        # Try to get the item at index 2
        try:
            id = int(path_params[2])
        except IndexError:
            pass  # No route parameter exists: /animals
        except ValueError:
            pass  # Request had trailing slash: /animals/

        return (resource, id)  # This is a tuple


    # Here's a class function
    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    # Here's a method on the class that overrides the parent's method.
    # It handles any GET request.
    def do_GET(self):
        self._set_headers(200)
        response = {}  # Default response

        # Parse the URL and capture the tuple that is returned
        (resource, id) = self.parse_url(self.path)

        resource_handlers = HANDLERS[resource]

        if(id is not None):
            response = f"{resource_handlers['get_single'](id)}"
        
        else:
            response = f"{resource_handlers['get_all']()}"

        self.wfile.write(response.encode())


    # Here's a method on the class that overrides the parent's method.
    # It handles any POST request.
    def do_POST(self):
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        # Convert JSON string to a Python dictionary
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
        self.do_POST()

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