import logging; logging.basicConfig(level=logging.INFO)

imporasyncio,os,json,time
from datetime import  datetime

from aiohttp import web

def index(request):
    return web.Response(boby=b'<h1>Awesome</h1>')

@asyncio.coroutine
def init(loop):
    app = web.Application(loop = loop)
    app.router.add_route('GET','/',index)
    srv = yield from loop.create_server(app.make_handler(),'127.0.0.1',9000)
    logging.info('server strated at http://127.0.0.1:9000')
    return sru
loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(init(loop))
finally:
    loop.run_forever()
