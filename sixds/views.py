from slovar import split_strip, slovar
from prf.view import BaseView
import random

import sixds.api as api
from sixds.model import Actors, ActorGraph

class InitView(BaseView):
    def show(self):
        return dict(
            initialized = api.INITIALIZED
        )

    def create(self):
        if api.INITIALIZED and not self._params.asbool('reload', default=False):
            raise ValueError('Already initialized. Use `reload=1` to re-initialize')

        settings = slovar(self.resource.config.get_settings())
        settings.has('movie_db_file',
                     err='`movie_db_file` is missing in configuration')

        api.init(settings['movie_db_file'])

class MoviesView(BaseView):
    def show(self, id):
        return dict(
            movie = id,
            cast = [it[1] for it in ActorGraph.edges([id])]
        )

    def create(self):
        api.add_movie(self._params.movie, self._params.aslist('actors'))

    def update(self, id):
        api.add_movie(id, self._params.aslist('actors'))


class RandomView(BaseView):
    def show(self):
        distances = []

        for actor in random.sample(Actors, 5):
            actors = [actor, 'Kevin Bacon']
            path = api.shortest_path(actors)
            movies = api.path_to_movies(path)
            distances.append(
                dict(
                    actors=actors,
                    distance=int(len(movies)),
                    path = path,
                    movies=movies,
            ))

        return distances


class DistanceView(BaseView):
    def show(self):
        self._params.aslist('actors')
        movies = []
        path = []

        if len(self._params.actors) == 1:
            self._params.actors.append('Kevin Bacon')

        if len(self._params.actors) == 2:
            path = api.shortest_path(self._params.actors)
            movies = api.path_to_movies(path)
        else:
            raise ValueError('must provide 1 or 2 actors')

        return dict(
            actors = self._params.actors,
            movies = movies,
            path = path,
            distance=int(len(movies))
        )
