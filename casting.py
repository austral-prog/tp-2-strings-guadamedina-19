def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    pass
    precio= int(input("Ingrese precio"))
    descuento= float(input("Ingrese descuento"))
    cantidad= int(input("Ingrese cantidad"))
    print(f"Precio: {precio}")
    print(f"Descuento: {descuento}")

    precio_descuento= precio - descuento
    print(f"Precio con descuento: {precio_descuento}")

    total= precio_descuento * cantidad
    print(f"Total: {total}")
