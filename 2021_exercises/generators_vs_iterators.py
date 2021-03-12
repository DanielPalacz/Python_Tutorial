import dis


def foofoo():
    x = 1
    return x


def drugiefoo():
    foofoo()


dis.dis(foofoo)
print("---------")
dis.dis(drugiefoo)




# Notatki podstawowe:

# return vs yield
# return -- konczy funkcje
# yield --- przerywa funcje ii wydaje element ( ii w obiekcie generatora jest zostawiony stan )



# Kiedy generator a kiedy iterator?


# generator:
# wtedy, gdy nie mozemy (nie chcemy) zajmowac bardzo duzo pamieci - stworzonymi już obiektami
# i chcemy musimy generować te obiekty dynamicznie
# jesli chodzi o mechanike dzialania:
# --- w kazdym kolejny cyklu -- tzn kiedy jest next wywolany
# --- yield wydaje coś (lub None) ii zawiesza dzialanie funcji (generatora)
# --- iii pozwala powrócić do tego momentu i wznowić działanie funkcji(generatora) przez wywolanie "next"
# ------------------------------------------------------------------------------------------------ next(generator)
# ------------------------------------------------------------------------------------------------ generator.__next__()

# generatory deklarujemy, tzn:
# g1 = generator() i g2 = generator()
# --> to są różne generatory

# iterator:
# - gdy dane istnieją (glownie sekwencje)
# - gdy oplaca nam sie stworzyc "mała" sekwencyjną strukturę
# --- it = iter(s)
# --- s: sekwencja, iter: funkcja z builtina zwracajca obiekt iteratora
# >>> next(it)
# 'a'
# >>> next(it)

# next dziala na obiekcie iteratora




def generator_numerow():
    number = 1000000
    while number < 2 * 10 ** 6:
        yield number
        number += 1
        if number == 1.5 * 10 ** 6:
            raise StopIteration

# print(dir(__builtins__))

# dwa rozne obiekty generatora
# takze beda dzialay niezaleznie
g1 = generator_numerow()
g2 = generator_numerow()

# tutaj tez 2 rozne obiekty
print(next(generator_numerow())) # nowo-stworzony nowy obiekt --> bo petla for tak dziala
for elem in generator_numerow():
    print(elem)
    if elem > 5:
        break


print("-------------------------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------------------")



print(next(generator_numerow()))

# tu zostal stw

slowo = "gugus"
print(type(iter(slowo)))
print(type(iter([2, 3, 4])))
