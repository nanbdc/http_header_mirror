#!/usr/bin/python3

"""HTTP server that reflects HTTP headers"""

import http.server
import html
import argparse

DEFAULT_ADDR = '127.0.0.1'
DEFAULT_PORT = 8099

class Reflector(http.server.BaseHTTPRequestHandler):
    """RequestHandler that displays all headers sent as part of GET requests"""
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        body_text = "<body><h1>Response headers:</h1><pre>" + html.escape(str(self.headers)) + "</pre></body>"
        self.wfile.write(bytes(body_text, "utf8"))

def launch_server(addr, port, Handler):
    """Launches the reflection server on the specified IP and port"""
    web_server = http.server.HTTPServer((addr, port), Handler)
    print("Connect to http://" + addr + ":" + str(port) + " to see headers. CTRL-C to quit.")
    web_server.serve_forever()

def parse_args():
    """Parses command line arguments and returns a tuple of (addr, port)"""
    parser = argparse.ArgumentParser(description="HTTP server that reflects HTTP headers")
    parser.add_argument("-a", "--addr", help="IP address to bind to", default=DEFAULT_ADDR)
    parser.add_argument("-p", "--port", help="port to bind to", type=int, default=DEFAULT_PORT)
    args = parser.parse_args()
    return (args.addr, args.port)

if __name__ == "__main__":
    addr, port = parse_args()
    launch_server(addr, port, Reflector)
