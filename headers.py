class Headers:
	def __init__(self):
		self.headers = {}

	def add_header(self, key, value):
		self.headers[key] = value

	# Just a convenient way to add multiple headers at once
	def add_headers(self, **kwargs):
		for key, value in kwargs.iteritems():
			self.add_header(key, value)

	# Properly formats HTTP headers so they can be appended to a response
	def to_headers(self):
		out = ""
		for key, value in self.headers.iteritems():
			out += "{0}: {1}\r\n".format(key, value)
		out += "\r\n"
		return out
