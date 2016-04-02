from aiohttp import web


class Home(web.View):

    async def get(self):
        print(self.request)
        return web.Response(body=b"Hello, world")

    async def post(self):
        pass
