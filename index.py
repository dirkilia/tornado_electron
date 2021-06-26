import tornado.web
import tornado.ioloop

class basicRequestHandler(tornado.web.RequestHandler):

    def get(self):
        self.write({'name': 'Ilia', 'surname': 'Vakhitov'})
        

if __name__ == '__main__':
    app = tornado.web.Application([
        (r"/", basicRequestHandler)
    ])

    app.listen(3000)
    tornado.ioloop.IOLoop.current().start()

