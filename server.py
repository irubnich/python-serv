import SocketServer
from handler import HTTPHandler
from headers import Headers

class Server:
	def __init__(self, port):
		self.web_root = './public'
		self.port = port

	def run(self):
		server = SocketServer.TCPServer(('localhost', self.port), HTTPHandler)
		server.web_root = self.web_root
		server.serve_forever()

server = Server(8081)
server.run()
