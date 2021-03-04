from pyramid.config import Configurator
from slovar import slovar
from sixds.api import init

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    with Configurator(settings=settings) as config:
        config = Configurator(settings=settings)
        config.include('prf')  # pyramid way of adding external packages.
        config.add_tween('prf.tweens.GET_tunneling')
        config.add_error_view(KeyError, error='Missing param: %s', error_attr='args')
        config.add_error_view(ValueError, error='Missing values: %s', error_attr='args')

        root = config.get_root_resource()  # acquire root resource.

        root.add_singular('init', view='sixds.views.InitView')
        root.add('movie', 'movies', view='sixds.views.MoviesView')
        root.add_singular('distance', view='sixds.views.DistanceView')
        root.add_singular('random', view='sixds.views.RandomView')

    config.scan()

    print('Frying the bacons...')

    settings = slovar(settings)
    settings.has('movie_db_file', err='`movie_db_file` is missing in configuration')
    api.init(settings['movie_db_file'], settings.get('db_size'))
    print('Your bacon is served !')

    return config.make_wsgi_app()
