# Maby shoulda made into a class and have self.inversion counted up
import os

def inversions():
  numbers = getList()
  sortedNumbers, inversions = inversionCounter(numbers, 0)
  print(sortedNumbers)
  print(inversions)

def inversionCounter(numbers, inversions):
  if(len(numbers) == 1):
    return numbers, inversions

  n = int(len(numbers)/2)
  left, leftI = inversionCounter(numbers[:n], inversions)
  right, rightI = inversionCounter(numbers[n:], inversions)
  inversions = leftI + rightI

  complete, l, r = [], 0, 0
  for i in range(len(numbers)):
    # This not working makes python CRRRINGE
    # le = (1000000, left[l])[l in range(0, len(left))] 
    # re = (1000000, right[r])[r in range(0, len(right))] 

    le, re = 1000000, 1000000
    if(l in range(0, len(left))):
      le = left[l]
    if(r in range(0, len(right))):
      re = right[r]

    if le < re:
      complete.append(le)
      l = l + 1
    else:
      complete.append(re)
      r = r + 1
      inversions = inversions + len(left) - l
    
  return complete, inversions

def getList():
  thisFolder = os.path.dirname(os.path.abspath(__file__))
  path = os.path.join(thisFolder, 'numbers.txt')
  f = open(path, 'r')
  numbers = f.readlines()

  numbersList = []
  for l in numbers:
    numbersList.append(int(l))

  return numbersList