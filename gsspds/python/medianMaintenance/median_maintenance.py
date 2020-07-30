from heapq import * # NOTE: heapq uses min heaps
import os

Hlow = [] # min heap multiplied by -1
Hhigh = [] # min heap
medians = []

folder = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(folder, 'data.txt')
with open(path) as file:
  data = file.readlines()
  for line in data:
    num = int(line)
    if not Hhigh or num < Hhigh[0]:
      num = num * -1
      heappush(Hlow, num)
    if not Hlow or num > abs(Hlow[0]):
      heappush(Hhigh, num)
    if len(Hlow)-2 >= len(Hhigh):
      num = abs(heappop(Hlow))
      heappush(Hhigh, num)
    if len(Hhigh)-2 >= len(Hlow):
      num = heappop(Hhigh) * -1
      heappush(Hlow, num)
    # TODO: Median counting
    if len(Hlow) >= len(Hhigh):
      medians.append(abs(Hlow[0]))
    else:
      medians.append(Hhigh[0])

file.close()

print(sum(medians) % 10000)