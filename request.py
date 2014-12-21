from server_exceptions import InvalidRequestException

class Request:
	ALLOWED_METHODS = ["GET", "HEAD"]

	def __init__(self, request_string):
		self.raw = request_string
		self.details = {}

		self.parse_request()

	def parse_request(self):
		# "GET / HTTP/1.1"
		attrs = self.raw.split(" ")
		self.details["method"] = attrs[0]
		self.details["path"] = attrs[1]
		self.details["version"] = attrs[2]

	def validate(self):
		if self.details["method"] not in self.ALLOWED_METHODS:
			raise InvalidRequestException("Server cannot handle a {} request.".format(self["method"]))

	# Override []
	def __getitem__(self, item):
		return self.details[item]

	def __str__(self):
		return self.raw
