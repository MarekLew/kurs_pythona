KOSZT_ZAKUPU = 1_000
kwota = input('Podaj kwotę: ')
kwota = float(kwota)
if kwota < KOSZT_ZAKUPU:
    print(f'Potrzebujesz jeszcze {(KOSZT_ZAKUPU - kwota)}💲')
