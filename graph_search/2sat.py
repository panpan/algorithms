'''
You are given a set of clauses where each clause is the disjunction of
two literals. You are looking for a way to assign a value "true" or
"false" to each of the variables so that all clauses are satisfied --
that is, there is at least one true literal in each clause. Design an
algorithm that determines whether or not a given 2SAT instance has a
satisfying assignment. Your algorithm should run in O(m+n) time,
where m and n are the number of clauses and variables, respectively.
'''

from collections import defaultdict
from a1 import kosaraju

def build_graph(f):
    g = defaultdict(list)
    g_rev = defaultdict(list)

    for x, y in f:
        edges = [(-x, y), (-y, x)]
        for u, v in edges:
            g[u].append(v)
            g_rev[v].append(u)

    return g, g_rev

def check_sccs(sccs):
    for scc in sccs:
        vs = [abs(v) for v in scc]
        if len(vs) > len(set(vs)):
            return False
    return True

if __name__ == '__main__':
    '''
    Each set of clauses (a 2-CNF formula) is represented as a list of
    tuples (x, y) where each variable or literal is a positive integer,
    negative if negated. The conjunction of disjunctions of pairs is
    computed. (Test cases taken from greatandlittle.com.)
    '''

    f1 = [(1, 1), (-1, 2), (-1, 3), (-2, -3), (4, 5)] # False
    f2 = [(1, 2), (-1, 3), (3, 4), (-2, -4)] # True
    f3 = [(-1, -4), (-2, -7), (2, -6), (2, 7), (-6, 7), (1, -5), (1, 7),
        (-5, 7), (-1, -7), (-3, 6), (3, -4), (3, -6), (-4, -6), (2, 5),
        (-2, 3), (-3, -5)] # False

    for f in [f1, f2, f3]:
        g, g_rev = build_graph(f)
        sccs = kosaraju(g, g_rev)
        print(check_sccs(sccs))
