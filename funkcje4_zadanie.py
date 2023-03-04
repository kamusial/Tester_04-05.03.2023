from funkcje2_kod import *
#https://docs.python.org/3/tutorial/errors.html

while True:
    wyplata = input('Ile zarabiasz? ')
    try:
        wyplata = float(wyplata)
        break
    except ValueError:
        print('zle dane, jeszcze raz')

liczba_dzieci = int(input('Ile masz dzieci? '))

print('kasa na osobę =',wyplata / (liczba_dzieci+2))
