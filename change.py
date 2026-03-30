def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """

    gasto= float(input("Ingrese gasto"))

    dinero_recibido= int(input("Ingrese dinero recibido"))
    print("Ingresar gasto:")
    print(gasto)
    print("Dinero recibido")
    print(dinero_recibido)
    print("")
    print("Vuelto")
    print("")
    vuelto= dinero_recibido - gasto
    print("Pesos:")
    print(int(vuelto))
    print("Centavos:")
    centavos= round(((float(vuelto) - int(vuelto)) * 100))
    print(centavos)


