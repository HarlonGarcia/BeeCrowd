cont = 1
maior = 0

while cont <= 100:
    x = int(input())
    if x > maior:
        maior = x
        posição = cont
    cont += 1

print('%i\n%i' % (maior, posição))
