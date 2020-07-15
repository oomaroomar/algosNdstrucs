import os 
import random
from utils import getAdjecencyList, findIndex

class Mincut:
  def __init__(self):
    self.count = 10
    self.redirects = {}

  def runKarger(self):
    for i in range(100):
      count = self.initMincutCount()
      if count < self.count:
        self.count = count
    return self.count

  def initMincutCount(self):
    directory = os.path.abspath(__file__)
    graph = getAdjecencyList(directory, 'graph.txt')
    self.redirects.clear()
    while len(graph) > 2:
      self.karger(graph)
    return self.countCuts(graph[0], graph[1])
    
  def karger(self, graph):
    uI = random.randint(0, len(graph) - 1)
    r2 = random.randint(1, len(graph[uI]) - 1)
    vinUi = self.getDestination(graph[uI][r2], graph[uI])
    vI = findIndex(lambda V: V[0] == vinUi, graph)
    if vI != None:
      self.nodeMerge(graph, uI, vI)
    else:
      print('FUCK')
      raise IndexError
      self.karger(graph)
    
  def nodeMerge(self, graph, u, v):
    for n in graph[u]:
      if n not in graph[v]:
        graph[v].append(n)
    self.redirects[graph[u][0]] = graph[v][0]
    graph.pop(u)

  def countCuts(self, arr1, arr2):
    count = 0
    for V in arr1:
      if V in arr2:
        count = count + 1
    
    return count
  
  def getDestination(self, value, check):
    d, pd = None, value
    while True:
      d = self.redirects.get(pd)
      print(d)
      if d == None:
        break
      elif d == pd:
        print(check)
      else:
        pd = d
    return pd