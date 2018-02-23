from tornado import web, ioloop, httpserver


class MainPageHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index.html')

class RegisterHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('register.html')

settings = {
    'template_path': 'templates',
}
application = web.Application([
            (r"/", MainPageHandler),
            (r"/register", RegisterHandler),
        ], **settings)

if __name__ == '__main__':
    http_server = httpserver.HTTPServer(application)
    http_server.listen(8888)
    ioloop.IOLoop.current().start()
