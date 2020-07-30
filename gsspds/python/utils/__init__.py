import os
import heapq

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
    for i in range(1, len(ili)):
      curValue = adjList.get(ili[0])
      if curValue == None:
        curValue = []
      adjList[ili[0]] = curValue + [ili[i]]

    # For revList
    for i in range(1, len(ili)):
      curValue = revList.get(ili[i])
      if curValue == None:
        curValue = []
      revList[ili[i]] = curValue + [ili[0]]
  file.close()
   
  return adjList, revList

def getAdjList(dirname, filename):
  folder = os.path.dirname(dirname)
  path = os.path.join(folder, filename)
  file = open(path, 'r')
  lines = file.readlines()
  adjList = {}
  for l in lines:
    li = l.split()
    adjList[int(li[0])] = []
    for ti in range(1, len(li)):
      adjList[int(li[0])].append(tuple(map(int, li[ti].split(',')))) 
  file.close()
  return adjList

def getHeapAdjList(dirname, filename):
  folder = os.path.dirname(dirname)
  path = os.path.join(folder, filename)
  file = open(path, 'r')
  lines = file.readlines()
  adjList = {}
  for l in lines:
    li = l.split()
    adjList[int(li[0])] = []
    for ti in range(1, len(li)):
      temp = tuple(map(int, li[ti].split(',')))
      adjList[int(li[0])].append(tuple([temp[1], temp[0]])) 
    heapq.heapify(adjList[int(li[0])])
  file.close()
  return adjList

def ansPrinter(result: dict):
  ans = ""
  ans = ans + str(result[7]) + ","+ str(result[37]) + ","\
    + str(result[59]) + ","+ str(result[82]) + ","\
    + str(result[99]) + ","+ str(result[115]) + ","\
    + str(result[133]) + ","\
    + str(result[165]) + ","\
    + str(result[188]) + ","\
    + str(result[197])
  print(ans)