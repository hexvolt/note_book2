import importlib

import aiohttp_debugtoolbar
from aiohttp import web

import settings as app_settings


class Application(web.Application):

    def __init__(self, settings, **kwargs):
        self.settings = settings

        super().__init__(middlewares=self.get_middleware_factories(),
                         debug=self.settings.DEBUG)

    def get_middleware_factories(self):
        """
        A generator that imports and returns middleware factories
        specified in the settings.py
        """
        for middleware in self.settings.MIDDLEWARE_FACTORIES:
            module_name, factory_name = middleware.rsplit('.', 1)

            module = importlib.import_module(module_name)

            yield getattr(module, factory_name)

    def setup(self):
        # setting up debug toolbar
        if self.settings.DEBUG:
            aiohttp_debugtoolbar.setup(self)

        # linking routes and resources
        app.router.add_route('GET', '/', hello)


async def hello(request):
    return web.Response(body=b"Hello, world")

app = Application(app_settings)
app.setup()


