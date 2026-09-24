def main():
    print("Hello from barberia-estilo-urbano!")


nombre = "carlos"
edad = 30
altura = 1.75
es_cliente = True

nombre_negocio = "Estilo Urbano"
precio_corte = 350
descuento_porcentage = 15
cliente_frecuente = False
primera_visita = False
def generar_bienvenida(
    nombre_negocio,
    precio_corte,
    cliente_frecuente,
    primera_visita 
):
    if precio_corte <= 0:
        return "Precio inválido"

    if primera_visita:
        precio_con_descuento = precio_corte - (precio_corte * 20 / 100)
        return (
            f"¡Bienvenido a {nombre_negocio}! "
            f"Tu corte cuesta ${precio_con_descuento:.2f} "
            "con tu descuento especial de primera visita."
        )

    if cliente_frecuente:
        precio_con_descuento = precio_corte - (precio_corte * 15 / 100)
        return (
            f"¡Bienvenido de nuevo a {nombre_negocio}! "
            f"Tu corte cuesta ${precio_con_descuento:.2f} "
            "con tu descuento de cliente frecuente."
        )

    return f"¡Bienvenido a {nombre_negocio}! Tu corte cuesta ${precio_corte:.2f}, sin descuento"


def generar_recibo(nombre_negocio, nombre_cliente, mensaje_Bienvenida):
    return (
        f"--- Recibo {nombre_negocio} --\n"
        f"Cliente: {nombre_cliente}\n"
        f"{mensaje_Bienvenida}"
    )


print(generar_recibo(nombre_negocio, "Carlos", generar_bienvenida(nombre_negocio, precio_corte, cliente_frecuente, primera_visita)))

print(generar_bienvenida("Estilo	Urbano",	350,	True,	True))


nombre_cliente	=	input("¿Cuál	es	tu	nombre?	")
respuesta_frecuente	=	input("¿Eres	cliente	frecuente?	(si/no)	")
respuesta_visita	=	input("¿Es	tu	primera	visita	este	mes?	(si/no)	")
es_frecuente	=	respuesta_frecuente.lower()	==	"si"
es_primera_visita	=	respuesta_visita.lower()	==	"si"
mensaje	=	generar_bienvenida("Estilo	Urbano",	350,	es_frecuente,	es_primera_visita)
print(generar_recibo(nombre_negocio, nombre_cliente, mensaje))