#Crear un programa que permita ingresar una lista de numeros al usuario y muestre por pantalla el maximo entre ambos numeros.

#Nota : Hacerlo con la función max(a,b) y luego con una comparación

#INICIO

lista=[]
for k in range(4):
    valor=int(input("Ingrese un valor:"))
    lista.append(valor)
mayor = max(lista)
print (mayor)

#FIN