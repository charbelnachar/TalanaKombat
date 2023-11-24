from typing import Optional
from typing import Tuple

from src.modules.personaje import Personaje
from src.modules.utility import Utility

class Simulacion():

    def definir_comienzo(self, player1: Personaje, player2: Personaje) -> Tuple[Personaje, Personaje]:
        """
        Define el comienzo de la pelea según las reglas establecidas.

        :param player1: Personaje 1.
        :param player2: Personaje 2.
        :return: Tupla con los personajes en orden de inicio.
        :rtype: tuple
        """
        utility = Utility()
        golpes_player1 = len(utility.quitar_cadenas_vacias(player1.get_golpes()))
        golpes_player2 = len(utility.quitar_cadenas_vacias(player2.get_golpes()))
        movi_player1 = len(utility.quitar_cadenas_vacias(player1.get_movimientos()))
        movi_player2 = len(utility.quitar_cadenas_vacias(player2.get_movimientos()))
        comb1 = golpes_player1 + movi_player1
        comb2 = golpes_player2 + movi_player2

        if comb1 > comb2:
            return player1, player2
        elif comb1 < comb2:
            return player2, player1
        else:
            if movi_player1 > movi_player2:
                return player2, player1
            elif movi_player1 < movi_player2:
                return player1, player2
            else:
                return player1, player2

    def definir_ganador(self, player1: Personaje, player2: Personaje) -> Optional[Personaje]:
        """
        Define al ganador de la pelea según las reglas establecidas.

        :param player1: Personaje 1.
        :param player2: Personaje 2.
        :return: El personaje ganador o None en caso de empate.
        :rtype: Optional[Personaje]
        """
        if player1.esta_vivo() and not player2.esta_vivo():
            return player1
        elif not player1.esta_vivo() and player2.esta_vivo():
            return player2
        elif player1.energia > player2.energia:
            return player1
        elif player1.energia < player2.energia:
            return player2
        else:
            return None

    def simular_pelea(self, player1: Personaje, player2: Personaje) -> None:
        """
        Simula una pelea entre dos personajes.

        :param player1: Personaje 1.
        :param player2: Personaje 2.
        """
        max_turnos = max(len(player1.get_movimientos()), len(player2.get_movimientos()))

        for i in range(max_turnos):
            comb_player1 = (player1.get_movimientos()[i] if i < len(player1.get_movimientos()) else "") + (
                player1.get_golpes()[i] if i < len(player1.get_golpes()) else "")

            comb_player2 = (player2.get_movimientos()[i] if i < len(player2.get_movimientos()) else "") + (
                player2.get_golpes()[i] if i < len(player2.get_golpes()) else "")

            player2.descontar_energia(player1.calcular_ataque(comb_player1))
            player1.narrar_movimiento(comb_player1)

            if player2.esta_vivo():
                player1.descontar_energia(player2.calcular_ataque(comb_player2))
                player2.narrar_movimiento(comb_player2)

            if not player1.esta_vivo() or not player2.esta_vivo():
                break

        ganador = self.definir_ganador(player1, player2)

        if ganador is not None:
            print(f"\n{ganador.nombre} gana la pelea y le queda {ganador.energia} de energía")
        else:
            print(f"\n{player1.nombre} y {player2.nombre} quedan empatados con {player2.energia} de energía")
