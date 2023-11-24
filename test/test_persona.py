import unittest
from unittest.mock import patch

from src.modules.personaje import Personaje


class TestPersonaje(unittest.TestCase):

    def setUp(self):
        self.movimientos_base = {"W": "Arriba", "S": "Abajo", "A": "Izquierda", "D": "Derecha"}
        self.golpes_base = {"P": {"nombre": "Puño", "energia": 1}, "K": {"nombre": "Patada", "energia": 1}}
        self.movimientos_especiales = {"DSD": {"nombre": "Taladoken", "energia": 3}}
        self.secuencia_golpes = {"movimientos": ["DSD"], "golpes": ["P"]}

    def test_esta_vivo_con_energia_positiva(self):
        personaje = Personaje(1, "Tonyn", 6, self.movimientos_especiales, self.secuencia_golpes)
        self.assertTrue(personaje.esta_vivo())

    def test_esta_vivo_con_energia_cero(self):
        personaje = Personaje(1, "Tonyn", 0, self.movimientos_especiales, self.secuencia_golpes)
        self.assertFalse(personaje.esta_vivo())

    def test_get_movimientos(self):
        personaje = Personaje(1, "Tonyn", 6, self.movimientos_especiales, self.secuencia_golpes)
        result = personaje.get_movimientos()
        self.assertEqual(result, ["DSD"])

    def test_get_golpes(self):
        personaje = Personaje(1, "Tonyn", 6, self.movimientos_especiales, self.secuencia_golpes)
        result = personaje.get_golpes()
        self.assertEqual(result, ["P"])

    def test_get_comb(self):
        personaje = Personaje(1, "Tonyn", 6, self.movimientos_especiales, self.secuencia_golpes)
        result = personaje.get_comb()
        self.assertEqual(result, ["DSD", "P"])

    def test_cast_golpes_basico_p(self):
        personaje = Personaje(1, "Tonyn", 6, self.movimientos_especiales, self.secuencia_golpes)
        result = personaje.cast_golpes_basico("P")
        self.assertEqual(result, "da un puñetazo")

    def test_cast_golpes_basico_k(self):
        personaje = Personaje(1, "Tonyn", 6, self.movimientos_especiales, self.secuencia_golpes)
        result = personaje.cast_golpes_basico("K")
        self.assertEqual(result, "da una patada")

    def test_cast_golpes_basico_otro(self):
        personaje = Personaje(1, "Tonyn", 6, self.movimientos_especiales, self.secuencia_golpes)
        result = personaje.cast_golpes_basico("Otro")
        self.assertEqual(result, "")

    def test_cast_movimiento_id_1_d(self):
        personaje = Personaje(1, "Tonyn", 6, self.movimientos_especiales, self.secuencia_golpes)
        result = personaje.cast_movimiento("D")
        self.assertEqual(result, "avanza")

    def test_cast_movimiento_id_2_d(self):
        personaje = Personaje(2, "Arnaldor", 6, self.movimientos_especiales, self.secuencia_golpes)
        result = personaje.cast_movimiento("D")
        self.assertEqual(result, "retrocede")

    def test_cast_movimiento_id_1_a(self):
        personaje = Personaje(1, "Tonyn", 6, self.movimientos_especiales, self.secuencia_golpes)
        result = personaje.cast_movimiento("A")
        self.assertEqual(result, "retrocede")

    def test_cast_movimiento_id_2_a(self):
        personaje = Personaje(2, "Arnaldor", 6, self.movimientos_especiales, self.secuencia_golpes)
        result = personaje.cast_movimiento("A")
        self.assertEqual(result, "avanza")

    def test_calcular_ataque_con_movimientos_especiales(self):
        personaje = Personaje(1, "Tonyn", 6, self.movimientos_especiales, self.secuencia_golpes)
        result = personaje.calcular_ataque("DSD")
        self.assertEqual(result, 3)

    def test_calcular_ataque_con_golpe_basico(self):
        personaje = Personaje(1, "Tonyn", 6, self.movimientos_especiales, self.secuencia_golpes)
        result = personaje.calcular_ataque("P")
        self.assertEqual(result, 1)

    def test_calcular_ataque_con_combinacion_vacia(self):
        personaje = Personaje(1, "Tonyn", 6, self.movimientos_especiales, self.secuencia_golpes)
        result = personaje.calcular_ataque("")
        self.assertEqual(result, 0)

    def test_narrar_movimiento_con_combinacion_valida(self):
        with patch("builtins.print") as mock_print:
            personaje = Personaje(1, "Tonyn", 6, self.movimientos_especiales, self.secuencia_golpes)
            personaje.narrar_movimiento("DSDP")
            mock_print.assert_called_with('➢Tonyn avanza, se agacha, avanza y da un puñetazo')

    def test_narrar_movimiento_con_combinacion_vacia(self):
        with patch("builtins.print") as mock_print:
            personaje = Personaje(1, "Tonyn", 6, self.movimientos_especiales, self.secuencia_golpes)
            personaje.narrar_movimiento("")
            mock_print.assert_called_with("➢Tonyn no hizo nada")

    # Agrega más pruebas según sea necesario.


if __name__ == '__main__':
    unittest.main()
