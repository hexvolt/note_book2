import importlib

import aiohttp_debugtoolbar
from aiohttp import web

import settings as settings_module
from routes import RouterConfiguration


class Application(web.Application):

    settings = None
    router_config = None

    def __init__(self, settings, **kwargs):
        self.settings = settings
        self.router_config = RouterConfiguration(self)

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

        if self.settings.DEBUG:
            aiohttp_debugtoolbar.setup(self)

        # configure application router
        self.router_config.link_routes()


application = Application(settings_module)
application.setup()


