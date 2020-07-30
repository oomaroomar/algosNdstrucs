import os

folder = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(folder, 'data.txt')

processed = {}
nuutti = {}
t = [i for i in range(-10000, 10001)]
ans = 0

with open(path) as file:
  data = file.readlines()
  for line in data:
    num = int(line)
    for i in t:
      if nuutti.get(i):
        continue
      if processed.get(i - num):
        ans = ans + 1
        nuutti[i] = True
    processed[num] = True
file.close()
print(ans)