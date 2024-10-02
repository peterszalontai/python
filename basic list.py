# Hozz létre három tömböt - listát!
# 1. érdemjegyeket tartalmazzon
# 2. az iskola osztályainak elnevezését tartalmazza
# 3. diákok adatait tartalmazza
erdemjegy = [1,2,3,4,5]
osztaly = ['9/ny',"9/a",'10/b','11/c','12/b','1/13b',"2/14b"]
adatok = ['Ákos','Dénes','Laci','levente','Neli','Regi']
print(osztaly)
print(erdemjegy)
print(adatok)

# Az előző feladatban létrehozott tömbök hermadik elemét adjuk az adott tömb
# 1. az első elem értékéül
# 2. a második elem értékéül
# 3. az utolsó elem értékéül

erdemjegy[0] = erdemjegy[2]
print(erdemjegy)
osztaly[1] = osztaly[2]
print(osztaly)
adatok[-1] = adatok[2]
adatok[len(adatok)-1] = adatok[2]
print(adatok)

# Írasd ki a tömbjeid hosszát és az elemeit egy sorban szóközzel elválaszva!
erdemjegy2=[1,2,3,4,5]
print (len(erdemjegy2) )
for x in erdemjegy2:
    print(x, end = ' ')
print()
# Távolítsd el a tömbökből az első elemet!
# 1. Az első tömbre használd a del parancsot
# 2. A második tömbre használd a pop() metódust és távolítsd el az utolsó elemet
# 3. A harmadik tömbre használd a remove() metódust

erdemjegy3= [1,2,3,4,5]
osztaly3 = ['9/ny',"9/a",'10/b','11/c','12/b','1/13b',"2/14b"]
adatok3= ['Ákos','Dénes','Laci','levente','Neli','Regi']
print(erdemjegy3)
del erdemjegy3[0]
print(erdemjegy3)
print(osztaly3)
osztaly3.pop(-1)
print(osztaly3)
print(adatok3)
adatok3.remove(adatok3[0])
print(adatok3)

# Adott az alábbi lista: [21, 32, 13, 44, 75] 
# 1. lépés: írjunk egy kódsort, amely megkérdezi a felhasználót, hogy melyik elemet mdosítsa a program.
# Az adott elemet módosítsd a felhasználó által megadott számra.
# 2. lépés: írjunk egy kódsort, amely eltávolítja az utolsó elemet a listából.
# 3. lépés: írjunk egy kódsort, amely kiírja a meglévő lista hosszát.
# 3. lépés: Írjunk kódot, mely kiírja sorban a lista elemeit. Soronként egye-egy elemet.

lista=[21,32,13,44,75]
szam = int (input('mondj egy számot.: '))
melyiket = int (input('melyik számra módosítsa? '))
index = melyiket - 1 
if index >= len(lista) or index < 0:
    print("nincs ilyen elem")
else:
    lista[index] = szam
print(lista)
lista.pop()
print(lista)

print(len(lista) )

for x in lista:
    print(x)

# Hozz létre egy programot, mely bekéri, hogy hány elemet szeretnél megadni, majd
# létrehoz egy listát és
# feltölti a tömböt a felhasználó által megadott értékekkel
# A lista elemeinek sorrendje egyezzen meg a felhasználó által megadott értékek sorrendjével!

# darab=int(input('add meg a számokat.:'))
# lista=[]
# for i in lista:
#     szam=int(input(adj meg egy értéket))

daran=int(input("add meg az elemeket"))
lista=[none] *darab
for i in range (darab):
    szam = int(input('kérek egy számot.:'))
    lista.insert(0,szam)
lista.reverse()
print(ista)