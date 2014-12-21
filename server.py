#!/usr/bin/env python

'''
Entry point for the server
'''

from os import environ
import SocketServer
from handler import HTTPHandler
from headers import Headers

class Server:
	def __init__(self, web_root, port):
		self.web_root = web_root
		self.port = port

	def run(self):
		server = SocketServer.TCPServer(('localhost', self.port), HTTPHandler)
		server.web_root = self.web_root
		server.serve_forever()

# Detect Heroku
try:
	port = int(environ['PORT'])
except KeyError as e:
	port = 8080 # Change this as necessary

server = Server('./public', port)
server.run()
