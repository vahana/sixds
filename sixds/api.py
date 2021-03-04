import pandas as pd
import ast
import networkx as nx

from prf.exc import HTTPNotFound

from sixds.model import ActorGraph, Actors


INITIALIZED = False

def init(file_name, size=None):
    global INITIALIZED

    try:
        df = pd.read_csv(file_name)
    except FileNotFoundError as er:
        raise KeyError(f'file not found: {er}')

    df['cast'] = df.cast.apply(ast.literal_eval)

    def build_the_graph(row):
        for actor in row.cast:
            name = actor['name']
            if name not in Actors:
                ActorGraph.add_node(name)
                Actors.add(name)

            ActorGraph.add_edge(row.title, name)

    if size:
        df = df[:int(size)]

    _ = df.apply(lambda r: build_the_graph(r), axis=1)

    INITIALIZED = True


def add_movie(movie, actors):
    for actor in actors:
        if actor not in Actors:
            ActorGraph.add_node(actor)
            Actors.add(actor)

        ActorGraph.add_edge(movie, actor)


def shortest_path(actors):
    try:
        return nx.shortest_path(ActorGraph, source=actors[0], target=actors[1])
    except (nx.exception.NodeNotFound, nx.exception.NetworkXNoPath):
        return []

def path_to_movies(path):
    return path[1::2]
