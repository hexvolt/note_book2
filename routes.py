from contextlib import contextmanager

from api import views as api_views
from core import views as core_views


class RouterConfiguration(object):

    def __init__(self, application):
        self.application = application

    @staticmethod
    def url_join(*paths):
        result = [path.strip('/') for path in paths[1:-1] if path]
        result.insert(0, paths[0].rstrip('/'))
        result.append(paths[-1].lstrip('/'))
        return '/'.join(result)

    @contextmanager
    def add_route_group(self, url_prefix, views_module, name_prefix=None):

        def add_route(url, view, http_method='*', name=None):
            view = getattr(views_module, view)

            url = self.url_join(url_prefix, url)
            name = ':'.join((name_prefix, name)) if name_prefix else name

            return self.application.router.add_route(http_method, url, view,
                                                     name=name)
        yield add_route

    def link_routes(self):
        """
        Connects all the routes described in this method to the Application.
        """
        # Core routes
        with self.add_route_group('', core_views) as add_route:
            add_route('/', 'Home', name='home')

        # API routes
        with self.add_route_group('/api', api_views, 'api') as add_route:
            add_route('/', 'Test', name='test')
