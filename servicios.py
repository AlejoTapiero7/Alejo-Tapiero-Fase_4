# Sistema Integral Software FJ
# Gestion de servicios especializados

from abc import abstractmethod
from entidades import Entidad
from excepciones import ErrorValidacion, ErrorServicio


class Servicio(Entidad):
    """Clase abstracta para representar los servicios."""

    def _init_(self, identificador, nombre, precio_base):
        super()._init_(identificador, nombre)

        if not isinstance(precio_base, (int, float)) or isinstance(precio_base, bool) or precio_base <= 0:
            raise ErrorValidacion("El precio base debe ser mayor que cero.")

        self._precio_base = precio_base

    @property
    def precio_base(self):
        return self._precio_base

    @abstractmethod
    def calcular_costo(self, duracion=1, impuesto=0, descuento=0):
        pass

    @abstractmethod
    def validar_parametros(self, duracion):
        pass


class ReservaSala(Servicio):
    """Servicio especializado en alquiler de salas."""

    def validar_parametros(self, duracion):
        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise ErrorServicio("La duracion de la sala debe ser positiva.")

    def calcular_costo(self, duracion=1, impuesto=0, descuento=0):
        self.validar_parametros(duracion)

        if impuesto < 0 or descuento < 0 or descuento > 100:
            raise ErrorServicio("Impuesto o descuento no valido.")

        subtotal = self.precio_base * duracion
        total = subtotal * (1 + impuesto / 100)
        return total * (1 - descuento / 100)

    def describir(self):
        return f"Sala: {self.nombre} | Precio por hora: ${self.precio_base:,.2f}"


class AlquilerEquipo(Servicio):
    """Servicio especializado en alquiler de equipos."""

    def validar_parametros(self, duracion):
        if not isinstance(duracion, int) or isinstance(duracion, bool) or duracion <= 0:
            raise ErrorServicio("La cantidad de dias debe ser un entero positivo.")

    def calcular_costo(self, duracion=1, impuesto=0, descuento=0):
        self.validar_parametros(duracion)

        if impuesto < 0 or descuento < 0 or descuento > 100:
            raise ErrorServicio("Impuesto o descuento no valido.")

        subtotal = self.precio_base * duracion
        total = subtotal * (1 + impuesto / 100)
        return total * (1 - descuento / 100)

    def describir(self):
        return f"Equipo: {self.nombre} | Precio por dia: ${self.precio_base:,.2f}"


class Asesoria(Servicio):
    """Servicio especializado en asesorias profesionales."""

    def validar_parametros(self, duracion):
        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise ErrorServicio("La duracion de la asesoria debe ser positiva.")

    def calcular_costo(self, duracion=1, impuesto=0, descuento=0):
        self.validar_parametros(duracion)

        if impuesto < 0 or descuento < 0 or descuento > 100:
            raise ErrorServicio("Impuesto o descuento no valido.")

        subtotal = self.precio_base * duracion
        total = subtotal * (1 + impuesto / 100)
        return total * (1 - descuento / 100)

    def describir(self):
        return f"Asesoria: {self.nombre} | Precio por hora: ${self.precio_base:,.2f}"