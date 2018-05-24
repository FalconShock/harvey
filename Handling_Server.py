#!/usr/bin/env python27

# Generate server.pem:
#   openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import subprocess, ssl

class S(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("<html><body>Hi !</body></html>")

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print (post_data)
        LVM_reply = subprocess.Popen("python summarizer.py", shell=True,\
        stdout=subprocess.PIPE).communicate()[0]
        print (LVM_reply)
        self._set_headers()
        self.wfile.write("<html><body>" + LVM_reply + "</body></html>")

def main(server_class = HTTPServer, handler_class = S, port = 80):

    print ("[+] Deploying Server.")
    server_addr = ('', port)
    httpd = server_class(server_addr,handler_class)
    print ("[+] Adding SSL Security.")
    httpd.socket = ssl.wrap_socket(httpd.socket, certfile = './server.pem', server_side = True)
    print ("[+] Started Serving.")
    httpd.serve_forever()

if __name__ == "__main__":

    from sys import argv

    if len(argv) == 2:
        main(port = int(argv[1]))
    else:
        main()
