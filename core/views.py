from aiohttp import web


class Home(web.View):

    async def get(self):
        return web.Response(body=b"Hello, world")
