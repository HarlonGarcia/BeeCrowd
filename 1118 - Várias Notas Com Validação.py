continuar = True
digitar_nota = True
novo_calculo = True
temp = 0
media = 0
cont = 0

while continuar:
    while digitar_nota:
        nota = float(input())
        
        if nota < 0 or nota > 10:
            print('nota invalida')
            
        else:
            temp += nota
            cont += 1

        if cont >= 2:
            digitar_nota = False
            novo_calculo = True
            media = temp / 2
            print('media = %.2f' % media)
    
    while novo_calculo:
        print('novo calculo (1-sim 2-nao)')
        ent = int(input())

        if ent == 1:
            digitar_nota = True
            novo_calculo = False
            cont = 0
            temp = 0
            media = 0
        elif ent == 2:
            continuar = False
            novo_calculo = False
