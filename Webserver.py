from http.server import HTTPServer, BaseHTTPRequestHandler

HOST = '127.0.0.1'
PORT = 9999

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/laurie"):
            self.send_response(302)
            self.send_header("Location", "https://tratt.net/laurie/")
            self.end_headers()
        else:
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Lokaler Server: Keine Weiterleitung.")

def start_server(host=HOST, port=PORT):
    server_address = (host, port)
    httpd = HTTPServer(server_address, MyHandler)
    print(f"[SERVER] Läuft auf http://{host}:{port}/")
    httpd.serve_forever()

start_server()