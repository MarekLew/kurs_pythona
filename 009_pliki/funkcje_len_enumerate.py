owoce = ['jabłko', 'banan', 'mandarynka', 'pitaja']
długość = len(owoce)
for i in range(0, długość):
    print(f'owoc pod indeksem {i} to {owoce[i]}')
pass

#robi to zamo
owoce = ['jabłko', 'banan', 'mandarynka', 'pitaja']
długość = len(owoce)
for i,owoc in enumerate(owoce):
    print(f'owoc pod indeksem {i} to {owoc}')
pass