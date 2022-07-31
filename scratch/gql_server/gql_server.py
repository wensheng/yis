import tornado.web
from tornado.ioloop import IOLoop

from graphene_tornado.tornado_graphql_handler import TornadoGraphQLHandler
from schema import schema


class ExampleApplication(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r'/graphql', TornadoGraphQLHandler, dict(graphiql=True, schema=schema)),
            (r'/graphql/batch', TornadoGraphQLHandler, dict(graphiql=True, schema=schema, batch=True)),
            (r'/graphql/graphiql', TornadoGraphQLHandler, dict(graphiql=True, schema=schema))
        ]
        tornado.web.Application.__init__(self, handlers)

if __name__ == '__main__':
    app = ExampleApplication()
    app.listen(5000)
    IOLoop.instance().start()
