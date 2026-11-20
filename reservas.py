# Sistema Integral Software FJ
# Gestion de reservas

from entidades import Entidad
from excepciones import ErrorReserva
from logs import registrar_evento, registrar_error


class Reserva(Entidad):
    """Clase encargada de gestionar las reservas."""

    def __init__(self, identificador, cliente, servicio, duracion):
        super().__init__(identificador, "Reserva")

        if cliente is None:
            raise ErrorReserva("Debe seleccionar un cliente.")

        if not isinstance(servicio, Entidad):
            raise ErrorReserva("El servicio seleccionado no es valido.")

        try:
            servicio.validar_parametros(duracion)
        except Exception as error:
            registrar_error(f"Error al validar la reserva: {error}")
            raise ErrorReserva("No fue posible validar la duracion.") from error

        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "Pendiente"

        registrar_evento(
            f"Reserva {identificador} creada para {cliente.nombre}."
        )

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def duracion(self):
        return self.__duracion

    @property
    def estado(self):
        return self.__estado

    def describir(self):
        return (
            f"Reserva {self.identificador} | "
            f"Cliente: {self.cliente.nombre} | "
            f"Servicio: {self.servicio.nombre} | "
            f"Duracion: {self.duracion} | "
            f"Estado: {self.estado}"
        )

    def confirmar(self):
        """Confirma una reserva pendiente."""

        if self.__estado != "Pendiente":
            raise ErrorReserva(
                "Solo se pueden confirmar reservas pendientes."
            )

        self.__estado = "Confirmada"
        registrar_evento(f"Reserva {self.identificador} confirmada.")
        return True

    def cancelar(self):
        """Cancela una reserva que no haya sido cancelada."""

        if self.__estado == "Cancelada":
            raise ErrorReserva("La reserva ya se encuentra cancelada.")

        self.__estado = "Cancelada"
        registrar_evento(f"Reserva {self.identificador} cancelada.")
        return True

    def procesar(self, impuesto=0, descuento=0):
        """Procesa la reserva y calcula su costo."""

        try:
            if self.__estado != "Pendiente":
                raise ErrorReserva(
                    "La reserva debe estar pendiente para procesarse."
                )

            costo = self.__servicio.calcular_costo(
                self.__duracion, impuesto, descuento
            )

            self.confirmar()

        except Exception as error:
            registrar_error(
                f"Error procesando reserva {self.identificador}: {error}"
            )
            raise ErrorReserva(
                "No se pudo completar el procesamiento de la reserva."
            ) from error

        else:
            registrar_evento(
                f"Reserva {self.identificador} procesada. "
                f"Costo total: ${costo:.2f}"
            )
            return costo

        finally:
            registrar_evento(
                f"Finalizo el intento de procesamiento "
                f"de la reserva {self.identificador}."
            )