from os.path import splitext, isdir, isfile, getsize
from urlparse import urlparse
import SocketServer

from server_exceptions import InvalidRequestException
from request import Request
from response import Response

class HTTPHandler(SocketServer.BaseRequestHandler):
	CONTENT_TYPES = {
		'html': 'text/html',
		'txt': 'text/plain',
		'png': 'image/png',
		'jpg': 'image/jpeg',
		'jpeg': 'image/jpeg',
		'pdf': 'application/pdf'
	}

	# Used to serve the appropriate MIME type in the headers
	def content_type(self, path):
		fileName, fileExtension = splitext(path)
		ext = fileExtension.split(".")[-1]
		if self.CONTENT_TYPES.has_key(ext):
			return self.CONTENT_TYPES[ext]
		else:
			return 'application/octet-stream'

	# Gets the filename from the requested path
	# Also takes care of a security issue with ".." in paths
	def requested_file(self, request_path):
		path = urlparse(request_path).path

		clean = []
		parts = path.split("/")
		for part in parts:
			if part == '' or part == '.':
				continue
			if part == '..':
				clean.pop()
			else:
				clean.append(part)

		# Assuming / is the filesystem separator, should work on OS X and Linux
		return "{0}/{1}".format(self.server.web_root, "".join(clean))

	# This is run on every single request within the event loop in server.py
	def handle(self):
		self.raw_request = self.request.recv(2048).strip()
		self.request_lines = self.raw_request.split('\r\n')

		# Log the request
		print "[{0}] {1}".format(self.client_address[0], self.request_lines[0])

		# The request itself is the first line, everything after it is a header
		# For example: GET / HTTP/1.1\r\n
		self.http_request = Request(self.request_lines[0])

		# The response is an object that gets serialized and written to the socket at the end of the server loop
		self.response = Response(self.http_request)

		try:
			# Check if the request method is allowed, as this is a limited server
			self.http_request.validate()

			# What file are we trying to load?
			path = self.requested_file(self.http_request.details["path"])

			# If it's a directory, try to load index.html
			if isdir(path):
				path = "{0}index.html".format(path)

			# Serve the file
			if isfile(path):
				with open(path) as file:
					headers = {
						"Content-Type": self.content_type(file.name),
						"Content-Length": getsize(file.name),
						"Connection": "close"
					}
					self.response.headers.add_headers(**headers)
					self.response.body = file.read()
			else: # Serve a 404
				self.response.set_code(404)
				self.response.body = "File not found\n"

				headers = {
					"Content-Type": "text/plain",
					"Content-Length": len(self.response.body),
					"Connection": "close"
				}
				self.response.headers.add_headers(**headers)
		except Exception as e:
			# Serve a 500 with the exception message
			self.response.set_code(500)
			self.response.body = e.value
		finally:
			# Make sure we write response to the socket regardless of if there were any errors
			self.request.sendall(self.response.__str__())
