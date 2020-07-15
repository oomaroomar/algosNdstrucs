import os 
import copy
import random
from utils import getAdjecencyList, findIndex

class Mincut2:
  def __init__(self):
    directory = os.path.abspath(__file__)
    adjMat, vertices, edges = getAdjecencyList(directory, 'graph.txt'), [], []
    for i in range(len(adjMat)):
      vertices.append(adjMat[i][0])
      for j in range(1, len(adjMat[i])):
        if [adjMat[i][0], adjMat[i][j]] not in edges:
          edges.append([adjMat[i][0], adjMat[i][j]])
    self.adjMat, self.vertices, self.edges = adjMat, vertices, edges
    
  def contract(self, ver, e):
    while len(ver) > 2:
      ind = random.randrange(0, len(e))
      [u, v] = e.pop(ind)
      ver.remove(v)
      newEdges = []
      for i in range(len(e)):
        if e[i][0] == v:
          e[i][0] = u
        elif e[i][1] == v:
          e[i][1] = u
        if e[i][0] != e[i][1]:
          newEdges.append(e[i])
      e = newEdges
    return len(e)
    
  def runKarger(self):
    results = []
    for i in range(200):
      v = copy.deepcopy(self.vertices)
      e = copy.deepcopy(self.edges)
      r = self.contract(v, e)
      results.append(r)
    return min(results)