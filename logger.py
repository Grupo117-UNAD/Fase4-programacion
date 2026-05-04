import logging

logging.basicConfig(
    filename='logs.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def registrar_evento(mensaje, nivel="INFO"):
    if nivel == "ERROR":
        logging.error(mensaje)
    else:
        logging.info(mensaje)