import os
import sys
import resource
from utils import getDirGraph

# Key = Leader, Value = Array of vertices
class SCC:
  def __init__(self):
    self.visited = set()
    self.sccs = {}
    self.indexValues = {}
    self.iv = 0
    self.s = None

  def start(self):
    sys.setrecursionlimit(10 ** 6)
    resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, 2 ** 30))
    directory = os.path.abspath(__file__)
    adjList, revList = getDirGraph(directory, 'demoscc.txt')
    self.kojaru(adjList, revList)
    print(self.sccs)
    # leaders = list(self.sccs.keys())
    # for key in leaders:
    #   print(len(self.sccs[key]))

  def kojaru(self, G, Grev):
    for v in Grev:
      if v not in self.visited:
        self.dfs1(Grev, v)
    self.visited.clear()
    del Grev
    for i in range(self.iv, 0, -1):
      self.s = i
      v = self.indexValues[i]
      # Get new vertex until find one that is unvisited
      if v in self.visited:
        continue
      self.dfs2(G, v)
    
  # First run ought to be on the reversed graph
  def dfs1(self, G, v):
    self.visited.add(v)
    if not G.get(v):
      return
    for edgeEnd in G[v]:
      if edgeEnd not in self.visited:
        self.dfs1(G, edgeEnd)
    self.iv = self.iv + 1
    # print(f'indexValues[{v}] = {self.iv}')
    self.indexValues[self.iv] = v

  def dfs2(self, G, v):
    self.visited.add(v)
    # Add vertex to it's leaders dictionary
    curValue = self.sccs.get(self.s)
    if curValue == None:
      curValue = []
    self.sccs[self.s] = curValue + [v]
    # Add vertex to it's leaders dictionary
    if not G.get(v):
      return
    for edgeEnd in G[v]:
      if edgeEnd not in self.visited:
        self.dfs2(G, edgeEnd)