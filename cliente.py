from excepciones import DatoInvalidoError

class Cliente:
    def __init__(self, cedula, nombre, email):
        if not cedula or not nombre or "@" not in email:
            raise DatoInvalidoError("Datos de cliente inválidos o incompletos[cite: 1].")
        self.__cedula = cedula  # Encapsulación[cite: 1]
        self.nombre = nombre
        self.email = email

    def mostrar_id(self):
        return self.__cedula