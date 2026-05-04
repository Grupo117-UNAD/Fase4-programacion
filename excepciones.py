class SoftwareFJError(Exception):
    """Clase base para el sistema."""
    pass

class DatoInvalidoError(SoftwareFJError):
    """Para parámetros faltantes o datos incorrectos."""
    pass

class OperacionNoPermitidaError(SoftwareFJError):
    """Para errores lógicos en reservas o cálculos."""
    pass