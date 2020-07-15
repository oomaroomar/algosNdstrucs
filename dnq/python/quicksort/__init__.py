import os
import statistics
from utils import getListFromFile

class qs:
  def __init__(self):
    self.count = 0

  def initQuicksort(self):
    directory = os.path.abspath(__file__)
    numbers = getListFromFile(directory, 'numbers.txt')
    # numbers = [3, 4, 1, 10, 2, 6]
    self.quickSort(numbers, 0, len(numbers))
    return numbers, self.count
  
  def partition(self, arr, l, r):
    # First as pivot
    # p = arr[l]

    # Last as pivot
    # p = arr[r-1] 
    # arr[l], arr[r-1] = arr[r-1], arr[l]

    distance = r - l
    p = None
    if distance <= 1:
      p = arr[l]
    else:
      halfD = int((distance - 1)/2)
      middle = l + halfD 
      p = statistics.median([arr[l], arr[middle], arr[r-1]])
      if p == arr[middle]:
        arr[l], arr[middle] = arr[middle], arr[l]
      elif p == arr[r-1]:
        arr[l], arr[r-1] = arr[r-1], arr[l]
    

    # This stays the same
    i = l + 1
    for j in range(l+1, r):
      if arr[j] < p:
        arr[i], arr[j] = arr[j], arr[i]
        i = i + 1
    arr[l], arr[i-1] = arr[i-1], arr[l]
    return i-1

  def quickSort(self, arr, l, r):
    if l < r:
      self.count = self.count + r - l - 1
      pIndex = self.partition(arr, l, r)
      self.quickSort(arr, l, pIndex)
      self.quickSort(arr, pIndex + 1, r)

  # failed attempt (works but the wrong way)
  def quicksort(self, arr):
    n = len(arr)
    if n <= 1:
      return arr
    self.count = self.count + n - 1
    less = []
    greater = []
    # first: arr[0]
    # last: arr[n-1]
    # first, middle, last median: statistics.median([arr[0], arr[n-1], arr[int(n/2)]])
    pivot = arr[0]
    for num in arr:
      if num > pivot:
        greater.append(num)
      elif num < pivot:
        less.append(num)

    return self.quicksort(less) + [pivot] + self.quicksort(greater)
