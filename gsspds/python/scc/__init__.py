import os
import sys
import resource
from utils import getDirGraph

class SCC:
  def __init__(self):
    self.visited = {}
    self.sccs = {}
    self.indexValues = {}
    self.iv = 0
    self.s = None
    self.adjList = {}
    self.revList = {}

  def start(self):
    sys.setrecursionlimit(10 ** 6)
    resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, 2 ** 30))
    directory = os.path.abspath(__file__)
    self.adjList, self.revList = getDirGraph(directory, 'scc.txt')
    self.kosajaru()
    ans = []
    leaders = list(self.sccs.keys())
    for key in leaders:
      ans.append(len(self.sccs[key]))
    ans.sort()
    for a in ans:
      print(a)

  def kosajaru(self):
    for v in self.revList:
      if not self.visited.get(v):
        self.dfs1(v)
    self.visited.clear()
    del self.revList
    for i in range(self.iv, 0, -1):
      self.s = i
      v = self.indexValues[i]
      # Get new vertex until find one that is unvisited
      if self.visited.get(v):
        continue
      self.dfs2(v)
    
  # First run ought to be on the reversed graph
  def dfs1(self, v):
    self.visited[v] = True
    if not self.revList.get(v):
      return
    for edgeEnd in self.revList[v]:
      if not self.visited.get(edgeEnd):
        self.dfs1(edgeEnd)
    self.iv = self.iv + 1
    self.indexValues[self.iv] = v

  def dfs2(self, v):
    self.visited[v] = True
    # Add vertex to it's leaders dictionary
    curValue = self.sccs.get(self.s)
    if curValue == None:
      curValue = []
    self.sccs[self.s] = curValue + [v]
    del curValue
    # Add vertex to it's leaders dictionary
    if not self.adjList.get(v):
      return
    for edgeEnd in self.adjList[v]:
      if not self.visited.get(edgeEnd):
        self.dfs2(edgeEnd)