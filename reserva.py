from logger import registrar_evento
from excepciones import OperacionNoPermitidaError

class Reserva:
    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Creada"

    def procesar_confirmacion(self):
        try:
            if self.duracion <= 0:
                raise OperacionNoPermitidaError("La duración debe ser mayor a cero[cite: 1].")
            costo = self.servicio.calcular_costo(self.duracion)
        except OperacionNoPermitidaError as e:
            registrar_evento(f"Fallo en reserva: {e}", "ERROR")
            self.estado = "Cancelada"
            raise  # Re-lanzar para el menú
        else:
            self.estado = "Confirmada"
            registrar_evento(f"Reserva exitosa: {self.cliente.nombre} - {costo}")
            return costo
        finally:
            print(f"Estado final de la operación: {self.estado}[cite: 1]")