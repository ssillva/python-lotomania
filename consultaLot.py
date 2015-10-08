import string
import sqlite3
import random
# Cria uma conexão e um cursor
con = sqlite3.connect('loteria.db')
cur = con.cursor()
s='sorteio'
c='concurso'

t = input("Digite o concurso => ")
lista = []
#pp =[]
#pi =[]
#ip =[]
#ii =[]
#def inclui(lista,num):
  #  if num not in lista and n < 100 and len(lista)<50:
    #        lista.append(num)
while len(lista) < 50:
    cur.execute('SELECT * FROM '+ s +' WHERE '+ c +'>= ?', (t,))
#print 'sorteios a partir do concurso', t, 'concursos:'
    for sorteio in cur.fetchall():
        print sorteio
        n =  random.choice(sorteio)
        #print n
 #       if n[0] in 13579:
   #         if n[1] in '13579':
     #           ii.append(n)
       #         inclui(lista, n)
         #   elif n[1] in '24680':
          #      ip.append(n)
          #      inclui(lista,n)
       # elif n[0] in '24680':
      #      if n[1] in '13579':
     #           pi.append(n)
     #           inclui(lista, n)
     #       elif n[1] in '24680':
     #           pp.append(n)
      #          inclui(lista,n)
        if n not in lista and n < 100 and len(lista)<50:
            lista.append(n)
            
lista.sort()
print lista
