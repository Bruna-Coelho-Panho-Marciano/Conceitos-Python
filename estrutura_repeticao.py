for c in range(0,4):
    print(c)

lista =[1, 2, 3, 4, 10]    
for numero in lista:
    mult = numero * 2
    print(mult)

soma = 0
cont= 0
for c in range(1, 6):
    num = int(input('Digite o {}o valor: '.format(c)))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('Você informou {} números pares e a soma entre eles é igual a {}'.format(cont, soma))

c = 1
while c <= 10:
    soma = c +10
    print(soma)
    c = c + 1
print('Fim')


