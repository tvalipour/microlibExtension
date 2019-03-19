import http.server
import socketserver
import request_handler

PORT = 8080

server_address = ("localhost", PORT)
server = http.server.HTTPServer(server_address, request_handler.RequestHandler)
server.serve_forever()