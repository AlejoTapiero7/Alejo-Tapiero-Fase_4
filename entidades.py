# Sistema Integral Software FJ
# Clases generales y gestion de clientes

from abc import ABC, abstractmethod
from excepciones import ErrorValidacion, ErrorCliente


class Entidad(ABC):
    """Clase abstracta que representa entidades generales."""

    def _init_(self, identificador, nombre):
        if not isinstance(identificador, int) or identificador <= 0:
            raise ErrorValidacion("El identificador debe ser un entero positivo.")

        if not isinstance(nombre, str) or not nombre.strip():
            raise ErrorValidacion("El nombre no puede estar vacio.")

        self._identificador = identificador
        self._nombre = nombre.strip()

    @property
    def identificador(self):
        return self._identificador

    @property
    def nombre(self):
        return self._nombre

    @abstractmethod
    def describir(self):
        """Metodo que deben implementar las clases derivadas."""
        pass


class Cliente(Entidad):
    """Clase que permite registrar y gestionar clientes."""

    def _init_(self, identificador, nombre, correo, telefono):
        super()._init_(identificador, nombre)

        if not isinstance(correo, str) or "@" not in correo:
            raise ErrorCliente("El correo electronico no es valido.")

        if not isinstance(telefono, str) or not telefono.isdigit():
            raise ErrorCliente("El telefono debe contener solo numeros.")

        if not 7 <= len(telefono) <= 15:
            raise ErrorCliente("El telefono debe tener entre 7 y 15 digitos.")

        self.__correo = correo.strip()
        self.__telefono = telefono

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    def describir(self):
        return (
            f"Cliente: {self.nombre} | "
            f"Correo: {self.__correo} | "
            f"Telefono: {self.__telefono}"
        )

    def actualizar_telefono(self, nuevo_telefono):
        """Actualiza el telefono despues de validar el dato."""

        if not isinstance(nuevo_telefono, str):
            raise ErrorCliente("El telefono debe ser texto.")

        if not nuevo_telefono.isdigit() or not 7 <= len(nuevo_telefono) <= 15:
            raise ErrorCliente("El nuevo telefono no es valido.")

        self.__telefono = nuevo_telefonos