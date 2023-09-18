import os 
from funciones import *
       
while True:
    imprimir_opciones()
    opcion = input("Seleccione una opción: ")
    match opcion:
        case "1":
            try:
                radio = float(input("Ingrese el radio del círculo: "))
                area = calcular_area_circulo(radio)
                print(f"El área del círculo es: {area:.1f}")
            except:
                print("Ingrese un radio válido")
            
        case "2":
            try:
                numero = int(input("Ingrese el número: "))
                if verificar_par_impar(numero):
                    print("Es par")
                else:
                    print("No es par")
            except:
                print("No es un número válido")
            
        case "3":
            try:
                lista = ingresar_lista_numerica()
                suma = suma_total_lista(lista)
                print(f"La suma total es: {suma}")
            except:
                print("Ingrese sólo valores numéricos")
            
        case "4":
            try:
                a = float(input("Ingrese el primer número: "))
                b = float(input("Ingrese el segundo número: "))
                c = float(input("Ingrese el tercer número: "))
                resultado = maximo_entre_tres(a,b,c)
                print(f"El máximo número es: {resultado}")
            except:
                print("Ingrese sólo números")
            
        case "5":
            cadena = input("Ingrese la cadena: ")
            print(invertir_cadena(cadena)) 
            
        case "6":
            try:
                lista = ingresar_lista_palabras()
                lista_ordenada = ordenar_alfabeticamente(lista)
                for elemento in lista_ordenada:
                    print(elemento)  
            except:
                print("Ingrese valores alfabéticos")
                
        case "7":
            try:
                base = float(input("Ingrese la base: "))
                exponente = float(input("Ingrese el exponente: "))
                resultado = calcular_potencia(base,exponente)
                print(f"La potencia de base {base} y exponente {exponente} es: {resultado}")
            except:
                print("Ingrese valores numéricos")
            
        case "8":
                lista = ingresar_lista_numerica()
                if lista:
                    for num in encontrar_num_pares(lista):
                        print(num)
                
        case "9":
            lista = ingresar_lista_numerica()
            if lista:
                resultado = calcular_producto_total(lista)
                print(f"El producto total es : {resultado}")
                
        case "10":
            cadena = input("Ingresar cadena: ")
            determinar_palindromo(cadena)   
            
        case "11":
            print("Adiós")
            break
        
    os.system("pause")




            
