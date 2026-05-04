from abc import ABC, abstractmethod
from excepciones import DatoInvalidoError

class EntidadSistema(ABC):
    """Clase abstracta general del sistema."""
    @abstractmethod
    def obtener_descripcion(self):
        pass

class Servicio(EntidadSistema):
    def __init__(self, nombre, costo_base):
        if costo_base <= 0:
            raise DatoInvalidoError("El costo base debe ser positivo.")
        self.nombre = nombre
        self.costo_base = costo_base

    @abstractmethod
    def calcular_costo(self, cantidad, impuesto=0.19, descuento=0):
        """Método para sobrecarga mediante parámetros opcionales[cite: 1]."""
        pass

class ReservaSala(Servicio):
    def calcular_costo(self, horas, impuesto=0.19, descuento=0):
        total = (self.costo_base * horas) * (1 + impuesto)
        return total - descuento

    def obtener_descripcion(self):
        return f"Servicio de Sala: {self.nombre}[cite: 1]"

class AlquilerEquipo(Servicio):
    def calcular_costo(self, dias, impuesto=0.19, descuento=0):
        return (self.costo_base * dias) * (1 + impuesto)

    def obtener_descripcion(self):
        return f"Alquiler de: {self.nombre}[cite: 1]"

class AsesoriaEspecializada(Servicio):
    def calcular_costo(self, sesiones, impuesto=0.19, descuento=0):
        return (self.costo_base * sesiones) * (1 + impuesto)

    def obtener_descripcion(self):
        return f"Asesoría: {self.nombre}[cite: 1]"