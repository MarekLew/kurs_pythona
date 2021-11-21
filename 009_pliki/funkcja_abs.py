while True:
    rok = input('Rok urodzenia: ')
    if not bool(rok.strip()):
        print('Musisz podać swój rok urodzenia')
        continue
    print(f'Twój rok urodzenia: {rok}')
    break
