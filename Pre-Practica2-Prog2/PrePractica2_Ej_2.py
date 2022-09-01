#Crear un programa que permita al usuario ingresar una lista de numeros. De esa lista de numeros almacenar en otra lista los numeros impares.

#El programa debe de mostrar por pantalla la lista de numeros originales y la lista de numeros impares.

#INICIO
lista=[]
listaimpar=[]
for k in range(4):
    valor=int(input("Ingrese un valor:"))
    lista.append(valor)
    if valor % 2 != 0:
        listaimpar.append(valor)
 
print (lista, listaimpar)
#FIN