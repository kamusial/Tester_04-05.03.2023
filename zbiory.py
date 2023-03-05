# załóżmy, że pesel ma 4 cyfry
# stwórzmy zbiór NFZ – ludzie, w bazie pacjentów NFZ
# stwórzmy zbiór chorzy_rok – ludzie chorzy w ostatnim roku
# stwórzmy zbiór chorzy_miesiac – ludzie chorzy w ostatnim miesiącu
# stwórzmy zbiór krzyki – wszystkich ludzi mieszkających na krzykach
# stwórzmy zbiór centrum – wszystkich ludzi mieszkających

NFZ = {1234, 3476, 4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243, 6435, 1298, 6732, 7688, 7648, 2345, 2356}
chorzy_rok = set([1234, 3476, 4544, 3423, 3254, 8769, 5436])
chorzy_miesiac = {1234, 3476, 3098, 4544, 3423}
krzyki = {4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243}
centrum = {7648, 2345, 2356, 3987, 1234, 3476, 3254}
zbior_pusty = set()
# intersection - część wspólna
# union - suma
# sprawdźmy, ile osób chorowało w ostatnim roku na krzykach
print('Chorzy w w ostatnim roku z krzyków to =',krzyki.intersection(chorzy_rok))
print('Liczba =',len(krzyki.intersection(chorzy_rok)))

# sprawdźmy ile osób z Krzyków chorowało w ostatnim roku
print('Chorzy w w ostatnim roku z krzyków to =',chorzy_rok.intersection(krzyki))
print('Liczba =',len(chorzy_rok.intersection(krzyki)))

# sprawdźmy, ile mieszka w sumie w centrum i na krzykach
# union - suma
print('liczba ludzi w centrum i na krzykac to',len(centrum.union(krzyki)))

# difference - rożnica 2 zbiorów     a.difference(b)
# sprawdźmy poprawność danych:
print ('\nPoprawność danych')
# każdy, kto chorował w ostatnim miesiącu, jednocześnie chorował w ostatnim roku

if len(chorzy_miesiac.difference(chorzy_rok)) == 0:
    print('ok')
else:
    print('problem', chorzy_miesiac.difference(chorzy_rok))

# nikt nie powinien mieszkać jendocześnie w centrum i na krzykach
# – jeśli tak, trzeba usunąć
# zbior.remove(element)

if len(krzyki.intersection(centrum)) != 0:
    x = input('Usinąć z centrum (C), czy z krzyków (K)? ')
    duplikaty = krzyki.intersection(centrum)
    if x.lower() == 'k':
        krzyki = krzyki.difference(duplikaty)
    elif x.lower() == 'c':
        for pesel in duplikaty:
            centrum.remove(pesel)
    else:
        print('zly wybor')
    print('Sprawdzam duplikaty: ',krzyki.intersection(centrum))

# każdy: chory, zdrowy, z krzyków i z centrum, powinien być w bazie NFZ.
# Jeśli nie ma, trzeba dopisać

# lista = [1, 2, 3, 3, 3, 4, 4, 4, 5]
# lista = list(set(lista))
# print(lista)
pozaNFZ = chorzy_rok.union(chorzy_miesiac.union(krzyki.union(centrum))).difference(NFZ)
if len(pozaNFZ) != 0:
    print(pozaNFZ)
    NFZ = NFZ.union(pozaNFZ)