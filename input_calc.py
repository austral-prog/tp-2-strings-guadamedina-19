def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """
    pass
    base= int(input("colocar base"))
    altura= int(input("colocar altura"))
    print(f"Base: {base}")
    print(f"Altura: {altura}")
    area= base * altura
    print(f"Area: {area}")
    perimetro = (base * 2) + (altura * 2)
    print(f"Perimetro: {perimetro}")
