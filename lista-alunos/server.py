import http.server
import socketserver
from sorteio import sorteioalunos 

PORT = 8004

def generate_html(data):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Simple List</title>
    </head>
    <body>
        <h1>List of Names and Ages</h1>
        <ul>
    """

    for name in data:
        html += f"<li>{name}</li>"

    html += """
        </ul>
    </body>
    </html>
    """
    
    return html


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        html = generate_html(sorteioalunos())  # Chame a função para gerar o HTML
        self.wfile.write(html.encode())

with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
