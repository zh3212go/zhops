import tornado.web
import tornado.httpserver
import tornado.ioloop
from tornado.options import options, define
import time

define(name="port", default=8888, help="run on the given port", type=int)


class addHandler1(tornado.web.RequestHandler):
    def get(self):
        input1 = self.get_argument("a", 0)
        input2 = self.get_argument("b", 0)
        #time.sleep(10)
        self.write("{result: %d}" % (int(input1) + int(input2)))

    def write_error(self, status_code, **kwargs):
        self.write("Gosh darnit, user! You caused a %d error." % status_code)


class addHandler2(tornado.web.RequestHandler):
    def get(self, input1, input2):
        self.write("{result: %d}" % (int(input1) + int(input2)))


def main():
    options.parse_command_line()
    app = tornado.web.Application(handlers=[(r'/add', addHandler1), (r'/add/(\d+)/(\d+)', addHandler2)])
    http_sever = tornado.httpserver.HTTPServer(app)
    http_sever.listen(options.port)
    print("Development server is running at http://0.0.0.0:%s" % options.port)
    print("Quit the server with Ctrl+C")
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
