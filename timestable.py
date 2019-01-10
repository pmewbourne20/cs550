i = []
for x in range(10):
  k = [0]*10
  i.append(k)
for x in range(10):
  i[0][x] = x
for y in range(10):
  i[y][0] = y
i[0][0] = "*"
for x in range(1,10):
  for y in range(1,10):
    i[y][x] = y*x 
for x in range(len(i)):
  print(i[x])