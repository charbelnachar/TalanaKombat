import json

class Utility():
    def quitar_cadenas_vacias(self, lista: list) -> list:
        """
        Este método elimina las cadenas vacías de una lista.

        :param lista: Lista que puede contener cadenas vacías.
        :type lista: list[str]
        :returns: Lista filtrada sin cadenas vacías.
        :rtype: list[str]
        """
        return [cadena for cadena in lista if cadena != ""]

    def leer_json(self, archivo: str) -> dict:
        """
        Este método lee un archivo JSON y devuelve los datos como un diccionario.

        :param archivo: Ruta del archivo JSON a leer.
        :type archivo: str
        :returns: Datos del archivo JSON como un diccionario.
        :rtype: dict
        """
        with open(archivo, "r") as f:
            datos = json.load(f)
        return datos

    def validar_dict(self,datos:dict)->bool:
        """
        Valida un diccionario que contiene movimientos y golpes para asegurar que cumple con las restricciones y el formato.

        :param datos: Diccionario con claves "player1" y "player2", cada uno con claves "movimientos" y "golpes".
        :type datos: dict
        :returns: True si los datos son válidos, False si no lo son.
        :rtype: bool
        """
        if not isinstance(datos, dict):
            print("Error: El argumento debe ser un diccionario.")
            return False

        players = ["player1", "player2"]

        for player in players:
            if player not in datos:
                print(f"Error: Falta la clave '{player}' en el diccionario.")
                return False

            player_data = datos[player]

            if not all(key in player_data for key in ["movimientos", "golpes"]):
                print(f"Error: Falta una o ambas claves 'movimientos' y 'golpes' en '{player}'.")
                return False

            movimientos = player_data["movimientos"]
            golpes = player_data["golpes"]

            # Validar movimientos
            for movimiento in movimientos:
                if not (isinstance(movimiento, str) and 0 <= len(movimiento) <= 5):
                    print(f"Error: Los movimientos en '{player}' deben ser cadenas de máximo 5 caracteres.")
                    return False

                if not (movimiento == "" or (movimiento.isupper() and all(letra in "WSAD" for letra in movimiento))):
                    print(
                        f"Error: Los movimientos en '{player}' solo pueden contener (W), (S), (A) o (D) en mayúsculas.")
                    return False

            # Validar golpes
            for golpe in golpes:
                if not (isinstance(golpe, str) and 0 <= len(golpe) <= 1):
                    print(f"Error: Los golpes en '{player}' deben ser cadenas de un solo carácter.")
                    return False

                if not (golpe == "" or (golpe.isupper() and golpe in ["P", "K"])):
                    print(f"Error: Los golpes en '{player}' solo pueden contener (P) o (K) en mayúsculas.")
                    return False

        return True