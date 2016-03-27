import asyncio

import aiohttp_debugtoolbar
from aiohttp_debugtoolbar import toolbar_middleware_factory
from aiohttp import web


async def hello(request):
    return web.Response(body=b"Hello, world")

app = web.Application(middlewares=[toolbar_middleware_factory], debug=True)
aiohttp_debugtoolbar.setup(app)

app.router.add_route('GET', '/', hello)

