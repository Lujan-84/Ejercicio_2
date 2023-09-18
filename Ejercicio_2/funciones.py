#Ejercicio 01: Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.
def calcular_area_circulo(radio:float)->float:
    area_circulo = round(3.1416 * radio**2,2)
    return area_circulo

#Ejercicio 02: Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.
def verificar_par_impar(num:int)->bool:
    respuesta = False
    try:
        if num % 2 == 0:
            respuesta = True
    except:
        respuesta = None
    return respuesta
    
#Ejercicio 03: Diseña una función que tome una lista de números y devuelva la suma de todos los elementos.
def suma_total_lista(lista:list)->float:
    acumulador_total = 0
    try:
        for e_lista in lista:
            acumulador_total += float(e_lista) 
    except:
        acumulador_total = None  
    return acumulador_total

#Ejercicio 04: Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.
def maximo_entre_tres(num_1:float,num_2:float,num_3:float)->float:
    lista = [num_1,num_2,num_3]
    maximo = lista[0]
    try:
        for num in lista:
            if num > maximo:
                maximo = num
    except:
        maximo = None
    return maximo

#Ejercicio 05: Escribe una función que tome una cadena como entrada y devuelva la cadena invertida.
def invertir_cadena(cadena:str)->str:
    cadena_invertida = ""
    for i in cadena:
        cadena_invertida = i + cadena_invertida
    return cadena_invertida

#Ejercicio 06: Crea una función que reciba una lista de palabras y devuelva una nueva lista con las palabras ordenadas alfabéticamente.
def ordenar_alfabeticamente(lista:list)->list:
    for i in range(len(lista)-1):
        for j in range((len(lista)-1)-i):
            if lista[j] > lista[j+1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
    return lista

#Ejercicio 07: Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.
def calcular_potencia(base:float,exp:float)->float:
    try:
        potencia = base**exp
    except:
        potencia = None
    return potencia


#Ejercicio 08: Define una función que reciba una lista de números y devuelva una nueva lista con solo los números pares.
def encontrar_num_pares(lista:list)->list:
    nueva_lista =[]
    try:
        for num in lista:
            if verificar_par_impar(num):
                nueva_lista.append(num)
    except:
        nueva_lista = None
    return nueva_lista

#Ejercicio 09: Escribe una función que tome una lista de números y calcule el producto de todos los elementos.
def calcular_producto_total(lista:list)->float:
    producto = 1
    try:
        for num in lista:
            producto *= num
    except:
        producto = None
    return producto
    
#Ejercicio 10: Crea una función que determine si una cadena dada es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).

def determinar_palindromo(cadena:str)->bool:
    resultado = False
    cadena_invertida = invertir_cadena(cadena)
    if cadena == cadena_invertida:
        resultado = True
    return resultado
    
    
    
def imprimir_opciones():
    print(f"1/Calcular área de un círculo.\t\t2/Verificar número par o impar.\n3/Suma total de una lista.\t\t4/Máximo entre tres números.\n5/Invertir cadena.\t\t\t6/Ordenar alfabéticamente.\n7/Potencia de un número.\t\t8/Seleccionar sólo pares.\n9/Producto total de una lista.\t\t10/Determinar palíndromo.\n11/Salir.")

def ingresar_lista_numerica()->list:
    lista_numeros = []
    while True:
        try:
            num = float(input("Ingrese un número a la lista: "))
        except:
            print("No es un dato válido")
            lista_numeros = None
            break
        lista_numeros.append(num)
        respuesta = input("Desea continuar? s/n: ")
        if respuesta != "s":
            break
    return lista_numeros

def ingresar_lista_palabras()->list:
    lista_general = []
    while True:
        elemento = input("Ingrese una palabra a la lista: ")
        if elemento.isdigit():
            lista_general = None
            break
        else:
            lista_general.append(elemento)
            respuesta = input("Desea continuar? s/n: ")
            if respuesta != "s":
                break
    return lista_general