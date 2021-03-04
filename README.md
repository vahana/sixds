#sixds
Six degree of separation.

sixds is an RESTful service built on top of prf framework that exposes various end points to play with becon distances.

###Python dependencies
```
pandas
networkx
prf
```

###Installation

1. create virtual env and activate it
2. `pip install -r requirements.txt`
3. `pserve development.ini`

###Usage

To list all endpoints:
`http://localhost:6543/_`

To test random actors with Kevin Bacon:
`http://localhost:6543/random`

To get distance between any 2 actors:
`http://localhost:6543/distance?actors=<comma-separated names>`
e.g. `http://localhost:6543/distance?actors=Brad+Pitt,Rossie+Cottrell`

To see actors in the movie:
`http://localhost:6543/movies/<movie name>`
e.g. `http://localhost:6543/movies/Tangled`

To add a new movie:
`http://localhost:6543/movies?_m=POST&movie=<movie_name>&actors=<comma separated names>`
e.g. `http://localhost:6543/movies?_m=POST&movie=XYZ&actors=Vahan,Kevin+Bacon`

To add an actor to an existing movie:
`http://localhost:6543/movies/<movie_name>?_m=PUT&actors=<comma-separated names>`
e.g. `http://localhost:6543/movies/XYZ?_m=PUT&actors=Julia,Bob`



*Data file used from: https://www.kaggle.com/tmdb/tmdb-movie-metadata*
