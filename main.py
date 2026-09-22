def main():
    print("Hello from barberia-estilo-urbano!")


if __name__ == "__main__":
    main()

nombre = "carlos"
edad = 30
altura = 1.75
es_cliente = True

#print(nombre)
#print(type(nombre))

nombre_negocio = "Estilo Urbano"
precio_corte = 350
descuento_porcentage = 15
cliente_frecuente = False

precio_con_descuento = precio_corte - (precio_corte * descuento_porcentage / 100)

if cliente_frecuente:
    mensaje = (
        f"¡Bienvenido de nuevo a {nombre_negocio}! "
        f"Tu corte con descuento cuesta ${precio_con_descuento:.2f} "
        "con tu descuento de cliente frecuente."
    )

    print(mensaje)
else:
    mensaje	=	f"¡Bienvenido	a	{nombre_negocio}!	Tu	corte	cuesta	${precio_corte:.2f}, sin descuento"

    print(mensaje)