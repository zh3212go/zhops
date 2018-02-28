import tornado.ioloop
import tornado.httpserver
import application
from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)


def main():
    options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application.app)
    http_server.listen(options.port)

    print("Development server is running at http://0.0.0.0:%s" % options.port)
    print("Quit the server with Control-C")

    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
