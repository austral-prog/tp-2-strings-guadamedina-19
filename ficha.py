from gettext import find


def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
    nombre = input("Ingrese nombre")
    email = input("Ingrese correo electronico")
    nota_1 = int(input("Ingrese nota uno"))
    nota_2 = int(input("Ingrese otra nota"))
    nota_3 = int(input("Ingrese otra nota"))

    print("""========================
    FICHA DEL ALUMNO
========================""")


    print(f"Nombre: {nombre.title().strip()}")

    print(f"Email: {email.lower()}")

    print(f"Caracteres en nombre: {len(nombre.strip())}")
    nombrestrip=nombre.strip()
    espacio = nombrestrip.find(" ")
    only_name= nombre.strip() [0:espacio]
    only_apellido= nombre.strip() [espacio +1: ]

    print(f"Iniciales: {only_name.upper()[0:1]}{only_apellido.upper()[0:1]}")
    nombre_inverso= nombrestrip [0:espacio]
    apellido_inverso= nombrestrip[espacio +1: ]
    print(f"Usuario: {apellido_inverso.lower()}.{nombre_inverso.lower()}")

    print(f"Email valido: {'@' in email}")
    arroba = email.find("@")

    print(f"Dominio: {email.lower() [arroba + 1 : :]}")

    print(f"Nombre para archivo: {nombrestrip.replace(" ","_").title()}")

    print(f"Cantidad de a: {nombre.lower().count("a")}")

    print(f"Codigo secreto: {nombrestrip.upper() [: : -1]}")
    print(f"Nota 1: {nota_1}")
    print(f"Nota 2: {nota_2}")
    print(f"Nota 3: {nota_3}")

    suma = nota_1 + nota_2 + nota_3
    print(f"Suma: {suma}")

    promedio = (nota_1 + nota_2 + nota_3)/ 3
    print(f"Promedio: {promedio}")

    promedio_entero= (nota_1 + nota_2 + nota_3)// 3
    print(f"Promedio entero: {promedio_entero}")

    print("="* 24 )








