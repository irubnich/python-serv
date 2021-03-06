from headers import Headers

class Response:
	CODES = {
		200: "OK",
		404: "Not Found",
		500: "Internal Server Error"
	}

	def __init__(self, request):
		self.request = request
		self.code = 200
		self.code_text = self.CODES[self.code]
		self.headers = Headers()

		if self.has_body():
			self.body = ""

	def set_code(self, code):
		self.code = code
		self.code_text = self.CODES[code]

	# The HEAD method doesn't have a body
	def has_body(self):
		return self.request["method"] != "HEAD"

	def __str__(self):
		s = "{0} {1} {2}\r\n".format(self.request["version"], self.code, self.code_text)
		s += self.headers.to_headers()
		if self.has_body():
			s += self.body
		return s
