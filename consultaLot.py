import string
import sqlite3
import random
# Cria uma conexão e um cursor
con = sqlite3.connect('loteria.db')
cur = con.cursor()
s='sorteio'
c='concurso'

t = input("Digite o concurso => ")
#lista armazenará numeros aleatorios para o jogo
lista = []
#pp =[]
#pi =[]
#ip =[]
#ii =[]
while len(lista) < 50:
    cur.execute('SELECT * FROM '+ s +' WHERE '+ c +'>= ?', (t,))
#print 'sorteios a partir do concurso', t, 'concursos:'
    for sorteio in cur.fetchall():
        print sorteio
        n =  random.choice(sorteio)
        #se numero nao estiver na lista e ainda está dentro da capacidade, ele adiciona numero na lista
        if n not in lista and n < 100 and len(lista)<50:
            lista.append(n)
            
#ordena a lista com numeros
lista.sort()
print lista
