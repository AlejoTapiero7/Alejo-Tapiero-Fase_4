# Sistema de registro de eventos y errores
import logging


# Configuración del archivo de registros
logging.basicConfig(
    filename="registros.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)


def registrar_evento(mensaje):
    """Registra los eventos importantes del sistema."""
    logging.info(mensaje)


def registrar_error(mensaje):
    """Registra los errores detectados durante la ejecución."""
    logging.error(mensaje)