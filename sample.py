from http.server import HTTPServer, BaseHTTPRequestHandler
content = """

<html>
<h1 allign="Center"> Laptop Cofiguration(GOPIKA-24900767) </h1>
<body>
<ol>
<li><b>Device name</b>	LAPTOP-ABTUIDF5
<li><b>Processor</b>	AMD Ryzen 5 5600H with Radeon Graphics            3.30 GHz
<li><b>Installed RAM</b>	16.0 GB (15.3 GB usable)
<li><b>Device ID</b></b>	E184BD74-16A1-441B-BB5E-29E4963BA6EB
<li><b>Product ID</b>	00342-42692-08817-AAOEM
<li><b>System type</b>	64-bit operating system, x64-based processor
<li><b>Pen and touch</b>	No pen or touch input is available for this display
</ol>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
