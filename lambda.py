def area_quadrado (L):
    area = L**2
    print(area)
area_quadrado(4)

area_quadrado2 = lambda x: x**2
print(area_quadrado2(7))

area_retangulo = lambda b, h: b*h
print(area_retangulo(4, 7))

# Uma vantagem é quando se utiliza juntamente com outros metodos
L =[4,5,6,7,11,9,10]
areas = list(map(lambda x: x**2, L))
print(areas)