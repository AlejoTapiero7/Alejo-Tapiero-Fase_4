# =====================================================
# SISTEMA INTEGRAL SOFTWARE FJ
# Gestion de clientes, servicios y reservas
# =====================================================

from entidades import Cliente
from servicios import ReservaSala, AlquilerEquipo, Asesoria
from reservas import Reserva
from excepciones import ErrorSistema
from logs import registrar_evento, registrar_error


# Listas internas para administrar la informacion
clientes = []
servicios = []
reservas = []


def registrar_cliente(cliente):
    """Registra un cliente en la lista interna."""

    if any(c.identificador == cliente.identificador for c in clientes):
        raise ErrorSistema("El cliente ya se encuentra registrado.")

    clientes.append(cliente)
    registrar_evento(f"Cliente registrado: {cliente.nombre}")
    print(f"Cliente {cliente.nombre} registrado correctamente.")


def registrar_servicio(servicio):
    """Registra un servicio disponible."""

    if any(s.identificador == servicio.identificador for s in servicios):
        raise ErrorSistema("El servicio ya se encuentra registrado.")

    servicios.append(servicio)
    registrar_evento(f"Servicio registrado: {servicio.nombre}")
    print(f"Servicio {servicio.nombre} registrado correctamente.")


def crear_reserva(identificador, cliente, servicio, duracion):
    """Crea y almacena una reserva."""

    reserva = Reserva(identificador, cliente, servicio, duracion)
    reservas.append(reserva)

    print("Reserva creada correctamente.")
    print(reserva.describir())

    return reserva


def ejecutar_operacion(numero, descripcion, funcion):
    """Ejecuta una operacion sin detener el programa ante errores."""

    print(f"\n--- OPERACION {numero}: {descripcion} ---")

    try:
        funcion()

    except Exception as error:
        registrar_error(f"Operacion {numero}: {error}")
        print(f"Error controlado: {error}")

    else:
        print("Operacion ejecutada correctamente.")

    finally:
        print(f"Fin de la operacion {numero}.")


# =====================================================
# PRUEBAS DEL SISTEMA: 10 OPERACIONES
# =====================================================

def prueba_1():
    cliente = Cliente(1, "Carlos Perez", "carlos@gmail.com", "3001234567")
    registrar_cliente(cliente)


def prueba_2():
    cliente = Cliente(2, "Maria Lopez", "maria@gmail.com", "3101234567")
    registrar_cliente(cliente)


def prueba_3():
    cliente = Cliente(3, "Juan Gomez", "correo_invalido", "3201234567")
    registrar_cliente(cliente)


def prueba_4():
    sala = ReservaSala(101, "Sala de reuniones", 50000)
    registrar_servicio(sala)


def prueba_5():
    equipo = AlquilerEquipo(102, "Computador portatil", 80000)
    registrar_servicio(equipo)


def prueba_6():
    asesoria = Asesoria(103, "Asesoria informatica", 100000)
    registrar_servicio(asesoria)


def prueba_7():
    reserva = crear_reserva(201, clientes[0], servicios[0], 2)
    costo = reserva.procesar(impuesto=19, descuento=10)
    print(f"Costo total de la reserva: ${costo:,.2f}")


def prueba_8():
    reserva = crear_reserva(202, clientes[1], servicios[1], 3)
    costo = reserva.procesar(impuesto=19)
    print(f"Costo total de la reserva: ${costo:,.2f}")


def prueba_9():
    crear_reserva(203, clientes[0], servicios[2], -2)


def prueba_10():
    reserva = crear_reserva(204, clientes[1], servicios[2], 2)
    reserva.cancelar()
    print("Estado final:", reserva.estado)


def mostrar_resumen():
    """Muestra el estado general del sistema."""

    print("\n====================================")
    print("RESUMEN GENERAL DEL SISTEMA SOFTWARE FJ")
    print("====================================")

    print("Clientes registrados:", len(clientes))
    print("Servicios registrados:", len(servicios))
    print("Reservas creadas:", len(reservas))

    print("\nLISTA DE CLIENTES:")
    for cliente in clientes:
        print(cliente.describir())

    print("\nLISTA DE SERVICIOS:")
    for servicio in servicios:
        print(servicio.describir())

    print("\nLISTA DE RESERVAS:")
    for reserva in reservas:
        print(reserva.describir())

    registrar_evento("Resumen general del sistema generado.")


def main():
    """Funcion principal del programa."""

    print("====================================")
    print(" BIENVENIDO AL SISTEMA SOFTWARE FJ")
    print("====================================")

    registrar_evento("Inicio del sistema Software FJ.")

    pruebas = [
        ("Registro de cliente valido", prueba_1),
        ("Registro de segundo cliente", prueba_2),
        ("Registro de cliente invalido", prueba_3),
        ("Creacion de reserva de sala", prueba_4),
        ("Creacion de alquiler de equipo", prueba_5),
        ("Creacion de asesoria", prueba_6),
        ("Reserva exitosa con descuento", prueba_7),
        ("Reserva exitosa de equipo", prueba_8),
        ("Reserva con duracion incorrecta", prueba_9),
        ("Creacion y cancelacion de reserva", prueba_10)
    ]

    for numero, (descripcion, funcion) in enumerate(pruebas, start=1):
        ejecutar_operacion(numero, descripcion, funcion)

    mostrar_resumen()

    print("\nSistema finalizado correctamente.")
    registrar_evento("Finalizacion del sistema Software FJ.")


if __name__ == "__main__":
    main()