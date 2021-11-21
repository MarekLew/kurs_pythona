f = open('mójplik.txt', 'w')
f.write('Zjadłem żabę i mam zgagę!')
f.close()

f = open('mójplik.txt')
print(f.read())
