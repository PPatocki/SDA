import SimpleHTTPServer
import SocketServer
#import yaml
#import os

#config = yaml.load(open("config.yml")) 
PORT=8000
#PORT=config['PORT']
#PATH=config['PATH']

#source_dir = os.path.join(os.path.dirname(__file__), PATH)
#os.chdir(source_dir)

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
