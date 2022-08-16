x = int(input())
cont = 0
soma = 0

while cont < x:
    n1, n2 = map(int, input() .split())
    menor = min(n1, n2)
    maior = max(n1, n2)

    if maior - menor == 1 or maior == menor or (maior - menor == 2 and maior % 2 != 0):
        print('0')
    else:
        if menor + 2 == maior and menor % 2 == 0:
            print(menor + 1)
        else:
            while menor < maior and menor + 2 != maior and menor + 1 != maior:
                if menor % 2 != 0:
                    menor += 2
                    soma += menor
                else:
                    menor += 1
                    soma += menor
                
            print(soma)
            soma = 0

    cont += 1
