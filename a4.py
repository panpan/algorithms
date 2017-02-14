from math import log
from copy import copy, deepcopy
from random import randrange

def karger_min_cut(graph, edges):
    while len(graph) > 2:
        u, v = rand_edge(graph, edges)
        edges -= len(graph[u]) + len(graph[v])
        graph[u] += graph[v]
        for w in graph[v]: # replace vs with us for other vertices
            graph[w].remove(v)
            graph[w].append(u)
        while u in graph[u]: # remove self loops
            graph[u].remove(u)
        edges += len(graph[u])
        del graph[v]
    return len(list(graph.values())[0])

def rand_edge(graph, edges):
    i = randrange(edges)
    for u, vs in graph.items():
        if len(vs) <= i:
            i -= len(vs)
        else:
            return u, vs[i]

if __name__ == '__main__':
    f = list(open('kargerMinCut.txt'))
    graph = {}
    edges = 0

    for i in range(len(f)):
        l = [int(v) for v in f[i].split()]
        graph[l[0]] = l[1:]
        edges += len(l[1:])

    n = len(graph)
    trials = int(n * n * log(n))
    min_cut = float('inf')

    for i in range(trials):
        g = deepcopy(graph)
        e = copy(edges)
        cut = karger_min_cut(g, e)
        if cut < min_cut:
            min_cut = cut
        print('trial:', i, ' cut:', cut, ' min_cut:', min_cut)
