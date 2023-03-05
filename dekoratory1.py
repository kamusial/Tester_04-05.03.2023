import datetime

def dodaj_date(func):
    def inner():
        teraz = datetime.datetime.now()
        print('Autualnie mamy',teraz.strftime('%H:%M:%S'))
        print('logowanie wlaczone')
        print('Funkcja napisana przez Kamila')
        func()
        print('koniec funkcji')
    return inner

@dodaj_date
def przywitanie():
    print('hejka')

przywitanie()


def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return
        return func(a, b)
    return inner

@smart_divide
def divide(a, b):
    print(a/b)

divide(5, 0)
divide(5, 2)



