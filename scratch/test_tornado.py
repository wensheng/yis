import sys
import asyncio

from tornado.web import Application, RequestHandler
from tornado.process import fork_processes
from tornado.httpserver import HTTPServer
from tornado.tcpserver import bind_sockets


if len(sys.argv) == 2:
    parallel = True
else:
    parallel = False


class MainHandler(RequestHandler):
    def get(self):
        self.write("Hello, world")


class ItemHandler(RequestHandler):
    def get(self, item_id):
        q = self.get_argument('q')
        self.write({'item_id': item_id, 'q': q})


def make_app():
    urls = [(r'/', MainHandler),
            (r'/items/(.*)', ItemHandler)]
    return Application(urls)


if parallel:
    sockets = bind_sockets(8888)
    fork_processes(4)


async def main():
    app = make_app()
    if parallel:
        server = HTTPServer(app)
        server.add_sockets(sockets)
    else:
        app.listen(8888)
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
