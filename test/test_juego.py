# test_juego.py
import unittest
from unittest.mock import patch
from src.modules.personaje import Personaje
from src.modules.juego import Simulacion


class TestSimulacion(unittest.TestCase):

    def setUp(self):
        self.utility_patch = patch('src.modules.utility')
        self.utility_mock = self.utility_patch.start()

    def tearDown(self):
        self.utility_patch.stop()

    def test_definir_comienzo_player1_mayor_combinaciones(self):
        player1 = Personaje(1, "Tonyn", 6, {'DSDP': {'energia': 3, 'nombre': 'Taladoken'}, 'SDK': {'energia': 2, 'nombre': 'Remuyuken'}}, {'golpes': ['K', 'P', 'P'], 'movimientos': ['SA', 'SA', 'SA']})
        player2 = Personaje(2, "Arnaldor", 6, {'ASAP': {'energia': 2, 'nombre': 'Taladoken'}, 'SAK': {'energia': 3, 'nombre': 'Remuyuken'}}, {'golpes': ['K', 'K'], 'movimientos': ['SA', 'ASA']})

        simulacion = Simulacion()
        result = simulacion.definir_comienzo(player1, player2)

        self.assertEqual(result, (player1, player2))

    def test_definir_comienzo_player2_mayor_combinaciones(self):
        player1 = Personaje(1, "Tonyn", 6, {'DSDP': {'energia': 3, 'nombre': 'Taladoken'}, 'SDK': {'energia': 2, 'nombre': 'Remuyuken'}}, {'movimientos': ["", "D", "SD"],'golpes': ["P", "", "K", "P"] })
        player2 = Personaje(2, "Arnaldor", 6, {'ASAP': {'energia': 2, 'nombre': 'Taladoken'}, 'SAK': {'energia': 3, 'nombre': 'Remuyuken'}}, {'golpes': ['K', 'K','K','K'], 'movimientos': ['SA','SA','SA' ,'ASA']})

        simulacion = Simulacion()
        result = simulacion.definir_comienzo(player1, player2)

        self.assertEqual(result, (player2, player1))

    def test_definir_comienzo_empate(self):
        player1 = Personaje(1, "Tonyn", 6, {'DSDP': {'energia': 3, 'nombre': 'Taladoken'}, 'SDK': {'energia': 2, 'nombre': 'Remuyuken'}}, {'golpes': ['K', 'P', 'P'], 'movimientos': ['SA', 'SA', 'SA']})
        player2 = Personaje(2, "Arnaldor", 6, {'ASAP': {'energia': 2, 'nombre': 'Taladoken'}, 'SAK': {'energia': 3, 'nombre': 'Remuyuken'}}, {'golpes': ['K', 'P', 'K'], 'movimientos': ['SA', 'ASA', 'DSD']})

        simulacion = Simulacion()
        result = simulacion.definir_comienzo(player1, player2)

        self.assertEqual(result, (player1, player2))

    def test_definir_comienzo_empate_movimientos(self):
        player1 = Personaje(1, "Tonyn", 6, {'DSDP': {'energia': 3, 'nombre': 'Taladoken'}, 'SDK': {'energia': 2, 'nombre': 'Remuyuken'}}, {'golpes': ['K', 'P', 'P'], 'movimientos': ['SA', 'SA', 'SA', 'A']})
        player2 = Personaje(2, "Arnaldor", 6, {'ASAP': {'energia': 2, 'nombre': 'Taladoken'}, 'SAK': {'energia': 3, 'nombre': 'Remuyuken'}}, {'golpes': ['K', 'K'], 'movimientos': ['SA', 'ASA']})

        simulacion = Simulacion()
        result = simulacion.definir_comienzo(player1, player2)

        self.assertEqual(result, (player1, player2))

    def test_definir_ganador_player1_gana(self):
        player1 = Personaje(1, "Tonyn", 6, {'DSDP': {'energia': 3, 'nombre': 'Taladoken'}, 'SDK': {'energia': 2, 'nombre': 'Remuyuken'}}, {'golpes': ['K', 'P', 'P'], 'movimientos': ['SA', 'SA', 'SA', 'A']})
        player2 = Personaje(2, "Arnaldor", 0, {'ASAP': {'energia': 2, 'nombre': 'Taladoken'}, 'SAK': {'energia': 3, 'nombre': 'Remuyuken'}}, {'golpes': ['K', 'K'], 'movimientos': ['SA', 'ASA']})

        simulacion = Simulacion()
        result = simulacion.definir_ganador(player1, player2)

        self.assertEqual(result, player1)

    def test_definir_ganador_player2_gana(self):
        player1 = Personaje(1, "Tonyn", 0, {'DSDP': {'energia': 3, 'nombre': 'Taladoken'}, 'SDK': {'energia': 2, 'nombre': 'Remuyuken'}}, {'golpes': ['K', 'P', 'P'], 'movimientos': ['SA', 'SA', 'SA', 'A']})
        player2 = Personaje(2, "Arnaldor", 6, {'ASAP': {'energia': 2, 'nombre': 'Taladoken'}, 'SAK': {'energia': 3, 'nombre': 'Remuyuken'}}, {'golpes': ['K', 'K'], 'movimientos': ['SA', 'ASA']})

        simulacion = Simulacion()
        result = simulacion.definir_ganador(player1, player2)

        self.assertEqual(result, player2)

    def test_definir_ganador_empate(self):
        player1 = Personaje(1, "Tonyn", 3, {'DSDP': {'energia': 3, 'nombre': 'Taladoken'}, 'SDK': {'energia': 2, 'nombre': 'Remuyuken'}}, {'golpes': ['K', 'P', 'P'], 'movimientos': ['SA', 'SA', 'SA', 'A']})
        player2 = Personaje(2, "Arnaldor", 3, {'ASAP': {'energia': 2, 'nombre': 'Taladoken'}, 'SAK': {'energia': 3, 'nombre': 'Remuyuken'}}, {'golpes': ['K', 'K'], 'movimientos': ['SA', 'ASA']})

        simulacion = Simulacion()
        result = simulacion.definir_ganador(player1, player2)

        self.assertIsNone(result)

    @patch('builtins.print')
    def test_simular_pelea_player1_gana(self, mock_print):
        player1 = Personaje(1, "Tonyn", 6, {'DSDP': {'energia': 3, 'nombre': 'Taladoken'}, 'SDK': {'energia': 2, 'nombre': 'Remuyuken'}}, {'golpes': ['K', 'P', 'P'], 'movimientos': ['SA', 'SA', 'SA', 'A']})
        player2 = Personaje(2, "Arnaldor", 0, {'ASAP': {'energia': 2, 'nombre': 'Taladoken'}, 'SAK': {'energia': 3, 'nombre': 'Remuyuken'}}, {'golpes': ['K', 'K'], 'movimientos': ['SA', 'ASA']})

        simulacion = Simulacion()
        simulacion.simular_pelea(player1, player2)

        mock_print.assert_called_with(f"\n{player1.nombre} gana la pelea y le queda {player1.energia} de energía")

    @patch('builtins.print')
    def test_simular_pelea_player2_gana(self, mock_print):
        player1 = Personaje(1, "Tonyn", 0, {'DSDP': {'energia': 3, 'nombre': 'Taladoken'}, 'SDK': {'energia': 2, 'nombre': 'Remuyuken'}}, {'golpes': ['K', 'P', 'P'], 'movimientos': ['SA', 'SA', 'SA', 'A']})
        player2 = Personaje(2, "Arnaldor", 6, {'ASAP': {'energia': 2, 'nombre': 'Taladoken'}, 'SAK': {'energia': 3, 'nombre': 'Remuyuken'}}, {'golpes': ['K', 'K'], 'movimientos': ['SA', 'ASA']})

        simulacion = Simulacion()
        simulacion.simular_pelea(player1, player2)

        mock_print.assert_called_with(f"\n{player2.nombre} gana la pelea y le queda {player2.energia} de energía")

    @patch('builtins.print')
    def test_simular_pelea_empate(self, mock_print):
        player1 = Personaje(1, "Tonyn", 3, {'DSDP': {'energia': 3, 'nombre': 'Taladoken'}, 'SDK': {'energia': 2, 'nombre': 'Remuyuken'}}, {'golpes': ['K', 'P'], 'movimientos': ['A', 'A']})
        player2 = Personaje(2, "Arnaldor", 3, {'ASAP': {'energia': 2, 'nombre': 'Taladoken'}, 'SAK': {'energia': 3, 'nombre': 'Remuyuken'}}, {'golpes': ['K', 'K'], 'movimientos': ['S', 'S']})

        simulacion = Simulacion()
        simulacion.simular_pelea(player1, player2)

        mock_print.assert_called_with(f"\n{player1.nombre} y {player2.nombre} quedan empatados con {player2.energia} de energía")


if __name__ == '__main__':
    unittest.main()
