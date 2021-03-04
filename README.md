# sixds
Six degree of separation.

sixds is a RESTful service built on top of [prf](https://github.com/vahana/prf) framework that exposes various end-points to play with becon distances.

### Python dependencies
```
pandas
networkx
prf
```

### Setup

1. `docker build -t sixds .`
2. `docker run --rm -it -p 6543:6543 sixds`

### Usage

#### List all endpoints:

http://localhost:6543/_

#### Random actors with Kevin Bacon:

http://localhost:6543/random

#### Distance between any 2 actors:

`http://localhost:6543/distance?actors=<comma-separated names>`

e.g. http://localhost:6543/distance?actors=Brad+Pitt,Rossie+Cottrell

#### Add a new movie with list of actors:

`http://localhost:6543/movies?_m=POST&movie=<movie_name>&actors=<comma separated names>`

http://localhost:6543/movies?_m=POST&movie=XYZ&actors=Vahan,Kevin+Bacon

#### Add actors to an existing movie:

`http://localhost:6543/movies/<movie_name>?_m=PUT&actors=<comma-separated names>`

e.g. http://localhost:6543/movies/XYZ?_m=PUT&actors=Julia,Bob

#### Fetch actors in the movie:

`http://localhost:6543/movies/<movie name>`

e.g. http://localhost:6543/movies/XYZ


*Data file used from: https://www.kaggle.com/tmdb/tmdb-movie-metadata*
