x = int(input())

for i in range(1, x+1):
  print(i, i*i, (i*(i*i)))
  for a in range(1):
    print(i, ((i*i)+1), ((i*(i*i))+1))
