# Excepciones personalizadas del sistema Software FJ

class ErrorSistema(Exception):
    """Clase base para los errores del sistema."""
    pass


class ErrorValidacion(ErrorSistema):
    """Se genera cuando un dato no cumple las validaciones."""
    pass


class ErrorCliente(ErrorSistema):
    """Se genera cuando existe un problema con un cliente."""
    pass


class ErrorServicio(ErrorSistema):
    """Se genera cuando un servicio no es válido o no está disponible."""
    pass


class ErrorReserva(ErrorSistema):
    """Se genera cuando ocurre un problema con una reserva."""
    pass