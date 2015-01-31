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
		response = list()
		for resource in resources:
			ranking = pc.rank(resource[1]).most_common()[0]
			response.append([resource[0],ranking[0],ranking[1]])
		
		self.wfile.write(json.dumps(response))
		self.wfile.close()


if __name__ == '__main__':
	try:
		server = HTTPServer(('',8001),ServiceHandler)
		print 'starting server...'
		server.serve_forever()
	except KeyboardInterrupt:
		print 'closing server...'
		server.socket.close();