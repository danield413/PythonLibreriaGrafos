from os import error
import json

class JSON:

    @staticmethod
    def cargar(ruta):
        try:
            with open(ruta) as file:
                data = json.load(file)
                return data
        except error:
            return None