import os

# directory = os.path.abspath(__file__)
def getListFromFile(directory, filename):
  thisFolder = os.path.dirname(directory)
  path = os.path.join(thisFolder, filename)
  f = open(path, 'r')
  lines = f.readlines()

  returnList = []
  for l in lines:
    returnList.append(int(l))

  return returnList

def getAdjecencyDict(directory, filename):
  folder = os.path.dirname(directory)
  path = os.path.join(folder, filename)
  f = open(path, 'r')
  lines = f.readlines()

  adjList = {}
  for l in lines:
    li = l.split()
    ili = list(map(int, li))
    adjList[ili[0]] = ili[1:]

  return adjList

def getAdjecencyList(directory, filename):
  folder = os.path.dirname(directory)
  path = os.path.join(folder, filename)
  f = open(path, 'r')
  lines = f.readlines()

  # 2d array where 1st element is a node and the rest are nodes the main node has connections to
  adjList = []
  for l in lines:
    li = l.split()
    ili = list(map(int, li))
    adjList.append(ili)
  
  return adjList

def find(pred, iterable):
  for element in iterable:
    if pred(element):
      return element
  return None

def findIndex(pred, iterable):
  for i in range(len(iterable)):
    if pred(iterable[i]):
      return i
  return None