from gevent.pywsgi import WSGIServer
from app import app
import requests

port = 3000

url = "https://pastebin.com/raw/D1iHsxXL"
r = requests.get(url)
content = r.text
print("\n" + content + "\n")
print(f"Server started. (Port: {port})")
http_server = WSGIServer(('', port), app)
http_server.serve_forever()