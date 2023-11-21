import http.server
import socketserver

# Define the port on which you want to run the server
PORT = 8081

# Create a custom request handler that handles POST requests
class FileUploadHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length)

        # Save the uploaded file to the current directory
        with open(self.path[1:], 'wb') as file:
            file.write(data)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'File uploaded successfully.')

# Create an HTTP server with the custom handler
with socketserver.TCPServer(("", PORT), FileUploadHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()

