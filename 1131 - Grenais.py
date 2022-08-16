go = True
gremio = 0
inter = 0
empates = 0
grenais = 0

while go:
    a, b = map(int, input() .split())
    if a > b:
        inter += 1
    elif a < b:
        gremio += 1
    else:
        empates += 1

    grenais += 1

    print('Novo grenal (1-sim 2-nao)')
    new = int(input())
    if new == 1:
        go = True
    else:
        go = False

print('%i grenais' % grenais)
print('Inter:%d' % inter)
print('Gremio:%i' % gremio)
print('Empates:%d' % empates)

if inter > gremio:
    print('Inter venceu mais')
elif gremio > inter:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')
