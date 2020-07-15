import os

def getDirGraph(dirname, filename):
  folder = os.path.dirname(dirname)
  path = os.path.join(folder, filename)
  file = open(path, 'r')
  lines = file.readlines()
  adjList = {}
  revList = {}
  for l in lines:
    li = l.split()
    ili = list(map(int, li))

    # For adjList
    curValue = adjList.get(ili[0])
    if curValue == None:
      curValue = []
    adjList[ili[0]] = curValue + [ili[1]]

    # For revList
    for i in range(1, len(ili)):
      curValue = revList.get(ili[i])
      if curValue == None:
        curValue = []
      revList[ili[i]] = curValue + [ili[0]]
   
  return adjList, revList