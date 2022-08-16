I = 0
J = 1
cont = 3

while I <= 2:
    while J <= cont:
        if I % 1 == 0:
            print('I=%i J=%i' % (I, J))
            J += 1
        else:
            print('I={:g} J={:g}'.format(I, J))
            J += 1

    J -= 2.8
    cont += 0.2
    I += 0.2
