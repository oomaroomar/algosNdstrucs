import os
import heapq
from utils import getHeapAdjList, ansPrinter

def start():
  directory = os.path.abspath(__file__)
  adjList = getHeapAdjList(directory, 'data.txt')

def dijkstra(G: dict):
  processed = {1: 0}
  i = 1
  while i < len(G) + 1: # O(n) # G starts at 1
    shortest = tuple([0, 1000000])
    for j in processed: # O(processed)
      for edge in G[j]:
        if edge[0] not in processed and processed[j] + edge[1] < shortest[1]:
          shortest = (edge[0], edge[1] + processed[j])
    processed[shortest[0]] = shortest[1]
    i = i + 1
  for j in range(1, 201):
    if j not in processed:
      processed[j] = 1000000
  return processed