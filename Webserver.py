from http.server import HTTPServer, BaseHTTPRequestHandler

HOST = '127.0.0.1'
PORT = 9999

class MyHandler(BaseHTTPRequestHandler): #Handler mit dem Server reagieren kann
    def do_GET(self):
        if self.path.startswith("/laurie"): 
            self.send_response(302) #302 temporäres weiterleiten auf Webseite
            self.send_header("Location", "https://tratt.net/laurie/") #Seie die aufgerufen wird
            self.end_headers()
        else:
            self.send_response(200) #200: success
            self.send_header("Content-type", "text/plain") #Header einstellen
            self.end_headers()
            self.wfile.write(b"Lokaler Server: Keine Weiterleitung.") #Was auf Seite steht

def start_server(host=HOST, port=PORT):
    server_address = (host, port) #Serveraddresse zusammensetzen
    httpd = HTTPServer(server_address, MyHandler) #Handler auf Serveradresse werfen, damit Server antworten kann
    print(f"[SERVER] Läuft auf http://{host}:{port}/")
    httpd.serve_forever() #läuft bis man ihn stoppt

start_server()