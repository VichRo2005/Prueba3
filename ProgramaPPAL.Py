import Archivo_funciones as funciones

personas = []


while True:
    print("Menú de opciones")
    print("1. Grabar")
    print("2. Buscar")
    print("3. Imprimir certificados")
    print("4. Salir")
    opcion = input("Ingrese la opción deseada: ")
    
    if opcion == "1":
        funciones.grabar_persona(personas)
    elif opcion == "2":
        funciones.buscar_persona(personas)
    elif opcion == "3":
        funciones.imprimir_certificados(personas)
    elif opcion == "4":
        funciones.salir_programa()
        break
    else:
        print("Opción inválida")