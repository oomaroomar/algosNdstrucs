def karatsuba(x,y):
  """Function to multiply 2 numbers in a more efficient manner than the grade school algorithm"""
  xSize = len(str(x))
  ySize = len(str(y))
  if xSize >= 3 or ySize >= 3:
    return x*y

  n = max(xSize, ySize)
  nby2 = n / 2

  b = x % 10**(nby2)
  a = (x - b)/(10**nby2)
  d = y % 10**(nby2)
  c = (y - d) / 10**(nby2)

  ac = karatsuba(a,c)
  bd = karatsuba(b,d)
  ad_plus_bc = karatsuba(a+b,c+d) - ac - bd
      
  # this little trick, writing n as 2*nby2 takes care of both even and odd n
  prod = ac * 10**(2*nby2) + (ad_plus_bc * 10**nby2) + bd

  return prod