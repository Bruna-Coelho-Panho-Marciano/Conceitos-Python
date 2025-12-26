# Otimiza a utilização de listas em Python e diminui a quantidade de linhas de código.
lista=[]
for valor in range(5):
    lista.append(valor + 10)
    print(lista)

lista = [valor + 10 for valor in range(5)]
print(lista)

lista = [valor+10 for valor in range(5)]
print(lista)

lista = []
for numero in range(1, 30):
    if numero % 4 == 0:
        lista.append(numero)
print(lista)

multiplos4 = [numero for numero in range(1,30) if numero % 4 == 0]
print(multiplos4)

conceito = ['azul' if nota >= 6 else 'vermelha' for nota in range(1,11)]
print(conceito)