def identificacao(nome, idade):
   print('Olá',nome,'\nVocê é jovem, tem apenas,',idade,'anos!')
   
identificacao('Bruna', 32)

def maior (x, y):
   if x < y:
      print('O maior número é ',y)
   elif x == y:
        print('Os números são iguais')
   else:
       print('O maior número é ',x)

maior(21, 16)

def pitagoras(cateto1, cateto2, hipotenusa):
    if hipotenusa == '?':
        hipotenusa = (cateto1**2 + cateto2**2)**(1/2)
        print('A hipotenusa é', hipotenusa)
    elif cateto1 == '?':
        cateto1 = (hipotenusa**2 - cateto2**2)**(1/2)
        print('O cateto1 é', cateto1)
    elif cateto2 == '?':
        cateto2 = (hipotenusa**2 - cateto1**2)**(1/2)
        print('O cateto2 é', cateto2)

pitagoras('?', 4, 5)
