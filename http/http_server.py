from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
from http.server import ThreadingHTTPServer
import json

PORT = 8081
IP = "192.168.242.136"

json_body = """{
    "data": {
        "events": {
            "ip": "192.168.242.136",
            "port": 8082
        },
        "model": "CITI 7587 3G CS7204MG",
        "nsd": {
            "name": "StartDisplay_6fbf37ed-d21b-49cf-b311-ea1b90e7b7b5",
            "type": "_startdisplay._tcp"
        },
        "uuid": "6fbf37ed-d21b-49cf-b311-ea1b90e7b7b5",
        "wifi": {
            "bssid": "1c:b7:2c:80:3e:f8",
            "ip": "192.168.242.136",
            "ssid": "ASUS-340"
        }
    },
    "error": 0
}"""


class HttpGetHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    """Обработчик с реализованным методом do_GET."""

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write('1'.encode())
        print("get")

    def do_POST(self):
        # content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        # post_data = self.rfile.read()  # <--- Gets the data itself
        # print(post_data)
        self._set_headers()
        self.wfile.write("{}".format(json_body).encode('utf-8'))
        print(self.headers)


def run(server_class=HTTPServer, handler_class=HttpGetHandler):
    server_address = ('', PORT)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()


if __name__ == '__main__':
    run(HTTPServer)


