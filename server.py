#!/usr/bin/env python

'''
Entry point for the server
'''

from os import environ
import SocketServer
from handler import HTTPHandler
from headers import Headers

class Server:
	def __init__(self, host, port, web_root):
		self.host = host
		self.port = port
		self.web_root = web_root

	def run(self):
		server = SocketServer.TCPServer((self.host, self.port), HTTPHandler)
		server.web_root = self.web_root
		server.serve_forever()

# Detect Heroku
try:
	port = int(environ['PORT'])
	host = '0.0.0.0'
except KeyError as e:
	# Change these as necessary
	port = 8080
	host = 'localhost'

server = Server(host, port, './public')
server.run()
