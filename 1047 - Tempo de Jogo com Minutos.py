h1, m1, h2, m2 = map(int, input() .split())

h = 0
m = 0

if h1 < h2 and m1 < m2:
    h = h2 - h1
    m = m2 - m1
    print('O JOGO DUROU %i HORA(S) E %i MINUTO(S)' % (h, m))
elif h1 == h2 and m1 == m2:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
elif h1 < h2 and m1 > m2:
    h = (h2 - h1) -1
    m = (60 - m1) + m2
    print('O JOGO DUROU %i HORA(S) E %i MINUTO(S)' % (h, m))
elif h1 > h2 and m1 < m2:
    h = (24 - h1) + h2
    m = m2 - m1
elif h1 == h2 and m1 < m2:
    h = 0
    m = m2 - m1
    print('O JOGO DUROU %i HORA(S) E %i MINUTO(S)' % (h, m))
else:
    h = ((24 - h1) + h2) - 1
    m = (60 - m1) + m2
    print('O JOGO DUROU %i HORA(S) E %i MINUTO(S)' % (h, m))
