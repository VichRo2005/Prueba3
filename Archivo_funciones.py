def validar_nif(nif, personas):
    """
    Función para validar el formato y la unicidad del NIF.
    Devuelve True si el NIF es válido y único y False en caso contrario.
    """
    # Verificar que el NIF tenga 12 caracteres
    if len(nif) != 12:
        return False
    
    # Verificar que los primeros 8 caracteres sean dígitos
    if not nif[:8].isdigit():
        return False
    
    # Verificar que el noveno caracter sea un guion
    if nif[8] != "-":
        return False
    
    # Verificar que los últimos 3 caracteres sean alfanuméricos
    if not nif[9:].isalnum():
        return False
    
    # Verificar que el NIF no esté repetido en la lista de personas
    for persona in personas:
        if persona["nif"] == nif:
            return False
    
    # Si todas las validaciones pasan, el NIF es válido y único
    return True


def validar_nombre(nombre):
    """
    Función para validar que el nombre no tenga números.
    Devuelve True si el nombre no tiene números y False en caso contrario.
    """
    return not any(char.isdigit() for char in nombre)


def grabar_persona(personas):
    """
    Función para grabar los datos de una persona.
    """
    nif = ""
    nombre = ""
    edad = -1
    
    while not validar_nif(nif, personas):
        nif = input("Ingrese el NIF de la persona: ")
        if not validar_nif(nif, personas):
            print("El NIF ingresado es inválido o ya se encuentra registrado en la base de datos.")
    
    while not validar_nombre(nombre) or len(nombre) < 8:
        nombre = input("Ingrese el nombre de la persona: ")
        if not validar_nombre(nombre):
            print("El nombre ingresado es inválido. No debe contener números.")
        elif len(nombre) < 8:
            print("El nombre debe tener al menos 8 caracteres")
    
    while edad < 0 or edad > 120:
        edad_str = input("Ingrese la edad de la persona: ")
        try:
            edad = int(edad_str)
            if edad < 0 or edad > 120:
                print("La edad debe estar entre 0 y 120 años.")
        except ValueError:
            print("La edad debe ser un número entero.")
    
    persona = {
        "nif": nif,
        "nombre": nombre,
        "edad": edad
    }
    personas.append(persona)
    print("Persona registrada correctamente")


def buscar_persona(personas):
    """
    Función para buscar una persona por su NIF.
    """
    nif_buscado = input("Ingrese el NIF de la persona que desea buscar: ")
    
    for persona in personas:
        if persona["nif"] == nif_buscado:
            print("NIF: ", persona["nif"])
            print("Nombre: ", persona["nombre"])
            print("Edad: ", persona["edad"])
            if persona["nif"][9:11] == "UE":
                print("La persona pertenece a la Unión Europea")
            else:
                print("La persona no pertenece a la Unión Europea")
            return
    
    print("No se encontró ninguna persona con el NIF indicado")


def imprimir_certificados(personas):
    """
    Función para imprimir los certificados solicitados.
    """
    nif = input("Ingrese el NIF de la persona para la que desea imprimir los certificados: ")
    
    for persona in personas:
        if persona["nif"] == nif:
            tipo_certificado = int(input("Ingrese el tipo de certificado que desea imprimir (1: Nacimiento, 2: Estado conyugal, 3: Pertenencia a la Unión Europea): "))
            print("Nombre: ", persona["nombre"])
            print("NIF: ", persona["nif"])
            print("Edad: ", persona["edad"])
            if tipo_certificado == 1:
                print("Tipo de Certificado a imprimir: Certificado de nacimiento.")
            elif tipo_certificado == 2:
                print("Tipo de Certificado a imprimir: Certificado de estado conyugal.")
            elif tipo_certificado == 3:
                if persona["nif"][9:11] == "UE":   
                    print("Tipo de Certificado a imprimir: Certificado de pertenencia a la Unión Europea.")
                else:
                    print("La persona no pertenece a la Unión Europea, no se puede imprimir el certificado.")
            else:
                print("Tipo de certificado inválido")
            return
    
    print("No se encontró ninguna persona con el NIF indicado")


def salir_programa():
    """
    Función para salir del programa.
    """
    print("Programa finalizado")
    print("""Autor: Vicente Rivera
    Versión: 1.0  /  Fecha: 21/JUN/2023""")
