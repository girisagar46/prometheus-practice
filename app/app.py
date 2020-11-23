import time
from http.server import BaseHTTPRequestHandler, HTTPServer

from prometheus_client import start_http_server, Counter, Gauge

REQUESTS = Counter('hello_world_total', 'Hello World requested.')
EXCEPTION = Counter('hello_world_exceptions_total', 'Exceptions serving hello world!')
SALES = Counter('hello_world_sales_euro_total', 'Euros made serving Hello World.')
INPROGRESS = Gauge('hello_world_inprogress', 'Number of hello worlds in progress')
LAST = Gauge('hello_world_last_time_seconds', 'The last time a Hello World was served')


class MyHandler(BaseHTTPRequestHandler):

    # REMIND: Can be uses as a decorator as well -> @EXCEPTIONS.count_exceptions()
    def do_GET(self):
        REQUESTS.inc()
        INPROGRESS.inc()
        # count_exceptions passes the exception up by raising it
        with EXCEPTION.count_exceptions():
            import random
            if random.random() < 0.2:
                raise Exception

        euros = random.random()
        SALES.inc(euros)
        self.send_response(200)
        self.end_headers()
        self.wfile.write("Hello World for {} euros.".format(euros).encode())
        LAST.set(time.time())
        INPROGRESS.dec()


if __name__ == '__main__':
    start_http_server(8000)
    server = HTTPServer(('localhost', 8001), MyHandler)
    server.serve_forever()
