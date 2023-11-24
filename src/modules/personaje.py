from typing import List, Dict, Union

class Personaje():
    """
    Clase que representa a un personaje en el juego Talana Kombat JRPG.

    Attributes:
    - id (int): Identificador único del personaje.
    - nombre (str): Nombre del personaje.
    - energia (int): Nivel de energía del personaje.
    - movimientos_especiales (dict): Diccionario de movimientos especiales del personaje.
    - secuencia_golpes (dict): Diccionario de la secuencia de golpes del personaje.
    """

    golpes_base: Dict[str, Dict[str, Union[str, int]]] = {
        "P": {"nombre": "Puño", "energia": 1},
        "K": {"nombre": "Patada", "energia": 1}
    }

    movimientos_base: Dict[str, str] = {
        "W": "Arriba", "S": "Abajo", "A": "Izquierda", "D": "Derecha"
    }

    def __init__(self, id: int, nombre: str, energia_inicial: int, movimientos: dict, sec_golpes: dict):
        """
        Constructor de la clase Personaje.

        :param id: Identificador único del personaje.
        :param nombre: Nombre del personaje.
        :param energia_inicial: Nivel inicial de energía del personaje.
        :param movimientos: Diccionario de movimientos especiales del personaje.
        :param sec_golpes: Diccionario de la secuencia de golpes del personaje.
        """
        self.id: int = id
        self.nombre: str = nombre
        self.energia: int = energia_inicial
        self.movimientos_especiales: dict = movimientos
        self.secuencia_golpes: dict = sec_golpes

    def descontar_energia(self, energia: int) -> None:
        """
        Descuenta energía al personaje.

        :param energia: Energía a descontar.
        """
        self.energia -= energia

    def calcular_ataque(self, combinacion: str) -> int:
        """
        Calcula la cantidad de energía que quita un ataque.

        :param combinacion: Combinación de movimientos y golpes.
        :return: Cantidad de energía que quita el ataque.
        :rtype: int
        """
        aux: str = ""
        if combinacion != "":
            for caracter in reversed(combinacion):
                aux = caracter + aux
                if aux in self.movimientos_especiales:
                    return self.movimientos_especiales[aux].get("energia")

            if combinacion[-1] in self.golpes_base:
                return self.golpes_base[combinacion[-1]].get("energia")
            else:
                return 0

        return 0

    def narrar_movimiento(self, ataque: str) -> None:
        """
        Narra un movimiento realizado por el personaje.

        :param ataque: Combinación de movimientos y golpes del ataque.
        """
        aux_attck: str = ""
        aux: str = ""
        flag: bool = True
        list_comb: List[str] = []

        if ataque:
            for caracter in ataque[::-1]:
                aux = caracter + aux

                if flag and aux in self.movimientos_especiales:
                    nombre_movimiento = self.movimientos_especiales[aux].get("nombre")
                    list_comb.append(f"conecta un {nombre_movimiento}")
                    flag = False
                    aux = ""
                elif not flag:
                    list_comb.append(self.cast_movimiento(caracter))

            list_comb.reverse()
            if flag:
                aux_menos: int = 0

                if ataque[-1] in self.golpes_base:
                    aux_attck = self.cast_golpes_basico(ataque[-1])
                    aux_menos = 1

                list_comb.extend(self.cast_movimiento(caracter) for caracter in ataque[:len(ataque) - aux_menos])

                if aux_attck:
                    list_comb.append(aux_attck)

            if len(list_comb) >= 2:
                string_list: str = ", ".join(list_comb[:-1]) + " y " + list_comb[-1]
            else:
                string_list: str = list_comb[0]

            print(f"➢{self.nombre} {string_list}")
        else:
            print(f"➢{self.nombre} no hizo nada")

    def esta_vivo(self) -> bool:
        """
        Verifica si el personaje está vivo.

        :return: True si el personaje está vivo, False en caso contrario.
        :rtype: bool
        """
        return self.energia > 0

    def get_movimientos(self) -> List[str]:
        """
        Obtiene la lista de movimientos del personaje.

        :return: Lista de movimientos del personaje.
        :rtype: list
        """
        return self.secuencia_golpes.get("movimientos")



    def get_golpes(self) -> List[str]:
        """
        Obtiene la lista de golpes del personaje.

        :return: Lista de golpes del personaje.
        :rtype: list
        """
        return self.secuencia_golpes.get("golpes")

    def get_comb(self) -> List[str]:
        """
        Obtiene la combinación de movimientos y golpes del personaje.

        :return: Combinación de movimientos y golpes del personaje.
        :rtype: list
        """
        return self.get_movimientos() + self.get_golpes()

    def cast_golpes_basico(self, gol: str) -> str:
        """
        Realiza el cast de golpes básicos.

        :param gol: Golpe básico a castear.
        :return: Mensaje del golpe básico.
        :rtype: str
        """
        if gol == "P":
            return "da un puñetazo"
        elif gol == "K":
            return "da una patada"
        else:
            return ""

    def cast_movimiento(self, mov: str) -> str:
        """
        Realiza el cast de movimientos.

        :param mov: Movimiento a castear.
        :return: Mensaje del movimiento.
        :rtype: str
        """
        if self.id == 1:
            if mov == "D":
                return "avanza"
            elif mov == "A":
                return "retrocede"
        if self.id == 2:
            if mov == "D":
                return "retrocede"
            elif mov == "A":
                return "avanza"
        if mov == "W":
            return "salta"
        elif mov == "S":
            return "se agacha"
