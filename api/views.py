from aiohttp import web


class Test(web.View):

    async def get(self):
        return web.Response(body=b"Test API call")

    async def post(self):
        pass
