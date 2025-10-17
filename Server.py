from http.server import HTTPServer, BaseHTTPRequestHandler

# aus Host und Port zusammengesetzte Serveraddresse
HOST = '127.0.0.1'
PORT = 9999

class MyHandler(BaseHTTPRequestHandler): #Handler mit dem Server reagieren kann
    def do_GET(self):
        self.send_response(200) #200: success
        self.send_header("Content-type", "text/plain") #Header einstellen
        self.end_headers()
        self.wfile.write(b"Alles OK: 200 Success!") #Was auf Seite steht

#Der Server der laufen soll
def start_server(host=HOST, port=PORT):
    server_address = (host, port) #Serveraddresse zusammensetzen
    httpd = HTTPServer(server_address, MyHandler) #Handler auf Serveradresse werfen, damit Server antworten kann
    print(f"[SERVER] Läuft auf http://{host}:{port}/")
    httpd.serve_forever() #läuft bis man ihn stoppt

start_server()