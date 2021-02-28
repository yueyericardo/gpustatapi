from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import gpustat
import argparse


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        data = gpustat.GPUStatCollection.new_query().jsonify()
        data['query_time'] = str(data['query_time'])
        self.wfile.write(json.dumps(data).encode(encoding='utf_8'))


def main():
    parser = argparse.ArgumentParser(description='Simple API Wrapper for gpustat')
    parser.add_argument('-p', '--port', type=int, default=8111)
    args = parser.parse_args()
    hostName = "0.0.0.0"
    serverPort = args.port
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")


if __name__ == "__main__":
    main()
