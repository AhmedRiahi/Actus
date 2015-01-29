from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from ResourcesCollector import ResourcesCollector
from PertinenceCalculator import PertinenceCalculator
import json

class ServiceHandler(BaseHTTPRequestHandler):

	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','application/json')
		self.send_header('Access-Control-Allow-Origin','*')
		self.end_headers()

		rc = ResourcesCollector()
		pc = PertinenceCalculator()

		resources = rc.snapshot()
		for resource in resources:

			self.wfile.write(json.dumps([resource[0],pc.rank(resource[1]).most_common()]))
			#self.wfile.write(pc.rank(resource[1]))


if __name__ == '__main__':
	try:
		server = HTTPServer(('',8001),ServiceHandler)
		print 'starting server...'
		server.serve_forever()
	except KeyboardInterrupt:
		print 'closing server...'
		server.socket.close();