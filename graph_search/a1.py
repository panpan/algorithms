'''
Implement Kosaraju's algorithm for computing the strongly connected
components of a directed graph. 'SCC.txt' contains the edges
(tail, head) of a directed graph. Vertices are labeled as positive
integers from 1 to 875714. Output the sizes of the 5 largest SCCs in
the given graph in decreasing order.
'''

import sys
import threading
from collections import defaultdict

def main():
    g = defaultdict(list)
    g_rev = defaultdict(list)

    for line in open('SCC.txt'):
        u, v = [int(v) for v in line.split()]
        g[u].append(v)
        g_rev[v].append(u)

    sccs = kosaraju(g, g_rev)
    sizes = [len(scc) for scc in sccs]
    res = sorted(sizes, reverse=True)[:5]
    while len(res) < 5:
        res.append(0)

    print(','.join([str(n) for n in res]))

def kosaraju(g, g_rev):
    dfs_loop1(g_rev)
    dfs_loop2(g)

    return leaders.values()

def dfs_loop1(g_rev):
    global t, explored, finishing_times

    t = 0
    explored = set()
    finishing_times = {}

    for i in list(g_rev):
        if i not in explored:
            dfs1(g_rev, i)

def dfs1(g_rev, i):
    global t, explored, finishing_times

    explored.add(i)

    for j in g_rev[i]:
        if j not in explored:
            dfs1(g_rev, j)

    t += 1
    finishing_times[i] = t

def dfs_loop2(g):
    global s, explored, leaders

    s = None
    explored = set()
    leaders = defaultdict(list)

    ordering = sorted(finishing_times, key=finishing_times.get,
                    reverse=True)

    for i in ordering:
        if i not in explored:
            s = i
            dfs2(g, i)

def dfs2(g, i):
    global explored, leaders

    explored.add(i)
    leaders[s].append(i)

    for j in g[i]:
        if j not in explored:
            dfs2(g, j)

if __name__ == '__main__':
    sys.setrecursionlimit(2**20)
    threading.stack_size(2**26)
    thread = threading.Thread(target=main)
    thread.start()
