def main():
    print("Hello from barberia-estilo-urbano!")


if __name__ == "__main__":
    main()

nombre = "carlos"
edad = 30
altura = 1.75
es_cliente = True

print(nombre)
print(type(nombre))

nombre_negocio = "Estilo Urbano"
precio_corte = 350
descuento_porcentage = 15
cliente_frecuente = True

precio_con_descuento = precio_corte - (precio_corte * descuento_porcentage / 100)

def generar_bienvenida(nombre_negocio, precio_corte, cliente_frecuente):
    if cliente_frecuente:
        precio_con_descuento = precio_corte - (precio_corte * 15 / 100)
        return (
            f"¡Bienvenido de nuevo a {nombre_negocio}! "
            f"Tu corte con descuento cuesta ${precio_con_descuento:.2f} "
            "con tu descuento de cliente frecuente."
        )

    return f"¡Bienvenido a {nombre_negocio}! Tu corte cuesta ${precio_corte:.2f}, sin descuento"


print(generar_bienvenida(nombre_negocio, precio_corte, cliente_frecuente))

print(generar_bienvenida("Estilo	Urbano",	350,	True))
print(generar_bienvenida("Estilo	Urbano",	350,	False))