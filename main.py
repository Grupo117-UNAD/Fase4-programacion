from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva
from logger import registrar_evento
import sys

def menu():#menu
    clientes = []
    servicios = [
        ReservaSala("Sala VIP", 100000),
        AlquilerEquipo("Proyector 4K", 50000),
        AsesoriaEspecializada("Consultoría Legal", 200000)
    ]
    
    print("\n--- SISTEMA DE GESTIÓN SOFTWARE FJ ---")
    
    while True:
        print("\n1. Registrar Cliente\n2. Crear Reserva\n3. Ver Logs\n4. Salir")
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                id_c = input("Cédula: ")
                nom = input("Nombre: ")
                mail = input("Email: ")
                nuevo_cli = Cliente(id_c, nom, mail)
                clientes.append(nuevo_cli)
                print("Cliente registrado con éxito.")

            elif opcion == "2":
                if not clientes:
                    print("Error: No hay clientes registrados.")
                    continue
                
                print("Servicios disponibles:")
                for i, s in enumerate(servicios):
                    print(f"{i}. {s.obtener_descripcion()}")
                
                idx_s = int(input("Seleccione índice del servicio: "))
                cant = int(input("Cantidad (horas/días/sesiones): "))
                
                res = Reserva(clientes[0], servicios[idx_s], cant)
                total = res.procesar_confirmacion()
                print(f"Reserva procesada. Total a pagar: ${total}")

            elif opcion == "3":
                with open("logs.txt", "r") as f:
                    print("\n--- CONTENIDO DE LOGS ---")
                    print(f.read())

            elif opcion == "4":
                print("Cerrando sistema...")
                break
        
        except Exception as e:
            registrar_evento(f"Error en menú: {e}", "ERROR")
            print(f"Ha ocurrido un error controlado: {e}")

if __name__ == "__main__":
    menu()