from http.server import BaseHTTPRequestHandler, HTTPServer

class FirewallRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        headers = self.headers
        content_length = int(headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode()

        # Suspicious indicators
        suspicious_path = "/tomcatwar.jsp"
        suspicious_headers = {
            "suffix": "%>//",
            "c1": "Runtime",
            "c2": "<%",
            "DNT": "1",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        if self.path == suspicious_path:
            self.send_response(403)
            self.end_headers()
            self.wfile.write(b"Blocked: Malicious path detected.")
            return

        for key, value in suspicious_headers.items():
            if headers.get(key) == value:
                self.send_response(403)
                self.end_headers()
                self.wfile.write(b"Blocked: Suspicious header detected.")
                return

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Request allowed.")

def run(server_class=HTTPServer, handler_class=FirewallRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Firewall server running on http://localhost:{port} ...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
