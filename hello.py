# ezt hívják commentnek
# ezek a sorok nem "programkódként" értelmeződnek az interpreter számára
# elsősorban arra használjuk, hogy megjegyzéseket fűzzünk a kódunkhoz
# hogy annak későbbi értelmezését segítsük

nev = input('írd be a neved: ')
print(f'Helló {nev}!')
print(f'Milyen szép név az, hogy {nev}!')
print(f'Szerintem már most Beléd vagyok zúgva {nev}! uwu <3')

valasz = input(f'{nev}, szeretsz programozni? ')
if valasz.lower() in {'igen', 'persze', 'ja', 'y', 'yes'}:
    print('Akkor még itt sokra viheted!')
else:
    print('Remélem akkor majd idővel megszereted... :(')

szam = int(input('Hányszor írjam ki a nevedet? '))
for x in range(szam):
    print(f'{nev}', end=' ')

print('\nRendben, végeztünk!')
print(f'Köszönj el szépen {nev}:', end= ' ')
while input() not in {'Szia!', 'Viszont látásra!'}:
    print('hát ez nem jött össze, próbáld újra:', end=' ')
print(f'Szia {nev}, legyen szép napod!')