#!/usr/bin/python


class Node(object):
    def __init__(self, name):
        self.name = name
        self.dist = {}

    def __repr__(self):
        return str(self.dist)

    def add_dist(self, peer, dist):
        self.dist[peer] = dist


class Solver(object):
    def __init__(self, nodes):
        self.visited = set()
        self.nodes = nodes
        self.shortest = None
        self.longest = 0
        self.curlen = 0

    def find_shortest(self, start):
        if len(self.visited) == len(self.nodes):
            if self.curlen < self.shortest or not self.shortest:
                self.shortest = self.curlen
            if self.curlen > self.longest:
                self.longest = self.curlen
            return (self.shortest, self.longest)

        for n, d in self.nodes[start].dist.iteritems():
            if n in self.visited:
                continue
            self.visited.add(n)
            self.curlen += d

            self.find_shortest(n)

            self.visited.remove(n)
            self.curlen -= d
        return (self.shortest, self.longest)



def read_nodes():
    nodes = {}
    i = open('advent9')
    for line in i:
        line = line.strip()
        peers, dist = line.split(' = ')
        dist = int(dist)
        a, b = peers.split(' to ')
        n = nodes.get(a, Node(a))
        n.add_dist(b, dist)
        nodes[a] = n
        n = nodes.get(b, Node(b))
        n.add_dist(a, dist)
        nodes[b] = n
    return nodes



def main():
    n = read_nodes()
    sol = Solver(n)
    short = 0
    lon = 0

    for start in n.keys():
      sol.visited.add(start)
      short, lon = sol.find_shortest(start)
      sol.visited.remove(start)
    print 'Shortest path is: %d' % short
    print 'Longest path is: %d' % lon

if __name__ == '__main__':
    main()
