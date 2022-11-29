import random

lista = [ ]

#1
'''
c = 2

for i in range(40):
    lista.append(c)
    c += 2

print(lista)
'''
#2
'''
for i in range(5):
    ind = int(input("Indique o índice da lista:"))
    n = float(input("Digite o valor a ser trocado:"))
    lista[ind] = n

print(lista)
'''
#3
'''
#a)
for i in range(5):
    sort_ind = random.randint(0,39)
    sort_num = random.randint(2,80)
    lista[sort_ind] = sort_num
print(lista)

#b)
s = 0
for e in lista:
    s += e
print(f"Soma = {s}")

#c)
for i in range(1,40):
    if lista[i] < lista[i-1]:
        print(f"Indice: {i} \nValor na lista:{lista[i]}")
        print("="*15)

'''
#4
'''
familia = [ ]
s = 0
n = int(input("Dite o total de pessoas presentes na sua família:"))
for i in range(n):
    idade = int(input("Digite a idade:"))
    familia.append(idade)
    s += idade
print(f"Idades da familia: {familia} \nSoma das idades: {s} anos")

#5
child = [ ]
adultos = [ ]
idosos = [ ]

for e in familia:
    if e >= 0 and e <=17:
        child.append(e)
    elif e <= 60:
        adultos.append(e)
    else:
        idosos.append(e)

print(f"Crianças: {child} \nAdultos: {adultos} \nIdosos: {idosos}")
'''

#5
tab = [ ]
for i in range(1, 41):
    tab.append(i)

for i in range(5):
    sort_ind = random.randint(0,39)
    tab[sort_ind] = 0
    print(sort_ind + 1, end=' ')


print(f"\n{tab}")

print("="*35)
cp = 1
cont = 1
contd = 1
while True:
    print(f"RODADA {cont}\nVocê está na casa {cp}")
    for i in range(3):
        print("Jogada", contd)
        dado = random.randint(1, 6)
        cp += dado
        if cp >= 40:
            print("Parabéns, você ganhou!")
            break
        print(f"O valor do dado foi {dado} \nFoi para a casa {cp}")  
        if(tab[cp - 1] == 0):
            print("Infelizmente, voltou para a casa 1.")
            cp = 1
        print(tab)
        print("="*35)
        contd += 1
    n = input()
    cont += 1
