import os
import sys
import resource
from utils import getDirGraph

# Key = Leader, Value = Array of vertices
class SCC:
  def __init__(self):
    self.visited = {}
    self.sccs = {}
    self.indexValues = {}
    self.iv = 0
    self.s = None

  def start(self):
    sys.setrecursionlimit(10 ** 6)
    resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, 2 ** 30))
    directory = os.path.abspath(__file__)
    adjList, revList = getDirGraph(directory, 'scc.txt')
    self.kojaru(adjList, revList)
    print(self.sccs)
    # leaders = list(self.sccs.keys())
    # for key in leaders:
    #   print(len(self.sccs[key]))

  def kojaru(self, G, Grev):
    for v in Grev:
      if not self.visited.get(v):
        self.dfs1(Grev, v)
    self.visited.clear()
    for i in range(len(self.indexValues), 0, -1):
      self.s = i
      v = self.indexValues[i]
      if self.visited.get(v): # Get new vertex until find one that is unvisited
        continue
      self.dfs2(G, v)
    
  # First run ought to be on the reversed graph
  def dfs1(self, G, v):
    self.visited[v] = True
    print(G.get(v))
    if not G.get(v):
      return
    for edgeEnd in G[v]:
      if not self.visited.get(edgeEnd): # If unvisited
        self.dfs1(G, edgeEnd)
    self.iv = self.iv + 1
    # print(f'indexValues[{v}] = {self.iv}')
    self.indexValues[v] = self.iv

  def dfs2(self, G, v):
    self.visited[v] = True
    # Add vertex to it's leaders dictionary
    curValue = self.sccs.get(self.s)
    if curValue == None:
      curValue = []
    self.sccs[self.s] = curValue + [v]
    # Add vertex to it's leaders dictionary
    for edgeEnd in G[v]:
      if not self.visited.get(edgeEnd): # If unvisited
        self.dfs2(G, edgeEnd)