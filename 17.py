def sumar(v1,v2,*lista):
    suma=v1+v2
    for x in range(len(lista)):
        suma=suma+lista[x]
    return suma

print("La suma de 10+20")
print(sumar(10,20))
print("La suma de 10+20+30+40")
print(sumar(10,20,30,40))
print("La suma de 10+20+30+40+50+60+70+80+90+100")
print(sumar(10,20,30,40,50,60,70,80,90,100))
