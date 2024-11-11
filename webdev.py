from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <body bgcolor="lavendercd">
         <h1 align="center"><u>device configurations</u></h1>
         <h2 align="center"><i>Mounika 24010589</i></h2>
           <ol type="1">
             <li>Device name:	Mounika</li>
             <li>Processor:	    13th Gen Intel(R) Core(TM) i5-1335U   1.30 GHz</li>
             <li>Installed RAM:	16.0 GB (15.7 GB usable)</li>
             <li>Device ID:	    15EEA3B2-7EF5-4DEC-903D-577382C3C005</li>
             <li>Product ID:	    00342-42709-01076-AAOEM</li>
             <li>System type:	64-bit operating system, x64-based processor</li>
             <li>Pen and touch:	No pen or touch input is available for this display</li>   
            
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