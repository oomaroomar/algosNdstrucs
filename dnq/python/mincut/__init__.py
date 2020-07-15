import os 
import copy
import random
from utils import getAdjecencyDict, findIndex

class Mincut:
  def runMinCut(self):
    directory = os.path.abspath(__file__)
    adjDict = getAdjecencyDict(directory, 'graph.txt')
    cuts = []
    for i in range(200):
      g = copy.deepcopy(adjDict)
      cut = self.kargerMinCut(g)
      cuts.append(cut)
    return min(cuts)

  def kargerMinCut(self, graph):
    while len(graph) > 2:
      v = random.choice(list(graph.keys()))
      w = random.choice(graph[v])
      self.contract(graph, v, w)
    return min(len(graph[list(graph.keys())[0]]), len(graph[list(graph.keys())[1]]))
      
  def contract(self, graph, v, w):
    for node in graph[w]:
      if node != v:
        graph[v].append(node)
        graph[node].append(v)
      graph[node].remove(w)
    del graph[w]