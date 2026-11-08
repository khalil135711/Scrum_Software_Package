"""Tiny local web server for Sprint Board. Usage: python serve.py [port]"""
import http.server, socketserver, sys, webbrowser, os

port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("127.0.0.1", port), Quiet) as httpd:
    url = f"http://localhost:{port}/"
    print(f"Sprint Board running at {url}  (Ctrl+C to stop)")
    webbrowser.open(url)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
