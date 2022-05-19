# -*- coding: utf-8 -*-

class Vertex:
    def _init__(self, key):
        self.id = key
        self.connectedTo = {}
    
    def addNeighbor(self, nbr, weight = 0):
        self.connectedTo[nbr] = weight
    
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
    
    def getConnections(self):
        return self.conntectedTo.keys()
    
    def getId(self):
        return self.id
    
    def getWeight(self, nbr):
        return self.connectedTo[nbr] 

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
    
    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    
    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    
    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, starting, ending, weight = 0):
        if starting not in self.vertList:
            nv = self.addVertex(starting)
        if ending not in self.vertList:
            nv = self.addVertex(ending)
        self.vertList[starting].addNeighbor(self.vertList[ending], weight)
    
    def getVertices(self):
        return self.vertList.keys()
    
    def __iter__(self):
        return iter(self.vertList.values())

def bfs(g: "Graph"):
    pass

def dfs(g: "Graph"):
    pass
