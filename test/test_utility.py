import json
import unittest
from unittest.mock import patch
from src.modules.utility import Utility

class TestUtility(unittest.TestCase):

    def setUp(self):
        self.utility = Utility()

    def test_quitar_cadenas_vacias(self):
        input_lista = ["", "movimiento1", "", "movimiento2", "", "movimiento3", ""]
        result = self.utility.quitar_cadenas_vacias(input_lista)
        self.assertEqual(result, ["movimiento1", "movimiento2", "movimiento3"])

    def test_quitar_cadenas_vacias_lista_vacia(self):
        input_lista = []
        result = self.utility.quitar_cadenas_vacias(input_lista)
        self.assertEqual(result, [])

    def test_leer_json(self):
        archivo = "test.json"
        mock_data = {"player1": {"movimientos": ["WASD", "WASD"], "golpes": ["P", "K"]},
                     "player2": {"movimientos": ["S", "D", "SA"], "golpes": ["P", "K"]}}

        with patch('builtins.open', create=True) as mock_open:
            mock_open().__enter__().read.return_value = json.dumps(mock_data)
            result = self.utility.leer_json(archivo)
            self.assertEqual(result, mock_data)



    def test_validar_dict(self):
        datos = {"player1": {"movimientos": ["WASD", "WASD"], "golpes": ["P", "K"]},
                 "player2": {"movimientos": ["S", "D", "SA"], "golpes": ["P", "K"]}}

        result = self.utility.validar_dict(datos)
        self.assertTrue(result)

    def test_validar_dict_formato_incorrecto(self):
        datos = {"player1": {"movimientos": ["WASD", "WASD"], "golpes": ["P", "K"]},
                 "player2": {"movimientos": ["S", "D", "SA"], "golpes": ["P", "K", "invalido"]}}

        result = self.utility.validar_dict(datos)
        self.assertFalse(result)

    def test_validar_dict_tipo_incorrecto(self):
        datos = "datos_invalidos"
        result = self.utility.validar_dict(datos)
        self.assertFalse(result)

    def test_validar_dict_clave_faltante(self):
        datos = {"player1": {"movimientos": ["WASD", "WASD"], "golpes": ["P", "K"]}}
        result = self.utility.validar_dict(datos)
        self.assertFalse(result)

    def test_validar_dict_clave_movimientos_faltante(self):
        datos = {"player1": {"golpes": ["P", "K"]}, "player2": {"movimientos": ["S", "D", "SA"], "golpes": ["P", "K"]}}
        result = self.utility.validar_dict(datos)
        self.assertFalse(result)

    def test_validar_dict_clave_golpes_faltante(self):
        datos = {"player1": {"movimientos": ["WASD", "WASD"]}, "player2": {"movimientos": ["S", "D", "SA"], "golpes": ["P", "K"]}}
        result = self.utility.validar_dict(datos)
        self.assertFalse(result)

    def test_validar_dict_movimientos_formato_incorrecto(self):
        datos = {"player1": {"movimientos": ["WASD", "WASD"], "golpes": ["P", "K"]},
                 "player2": {"movimientos": ["S", "D", "SA", "invalido"], "golpes": ["P", "K"]}}
        result = self.utility.validar_dict(datos)
        self.assertFalse(result)

    def test_validar_dict_movimientos_longitud_incorrecta(self):
        datos = {"player1": {"movimientos": ["WAAAASD", "WASD"], "golpes": ["P", "K"]},
                 "player2": {"movimientos": ["SDDDDD", "D", "SA", "WASD"], "golpes": ["P", "K"]}}
        result = self.utility.validar_dict(datos)
        self.assertFalse(result)

    def test_validar_dict_movimientos_caracter_invalido(self):
        datos = {"player1": {"movimientos": ["WASD", "WASD"], "golpes": ["P", "K"]},
                 "player2": {"movimientos": ["S", "D", "INVALIDO"], "golpes": ["P", "K"]}}
        result = self.utility.validar_dict(datos)
        self.assertFalse(result)

    def test_validar_dict_golpes_formato_incorrecto(self):
        datos = {"player1": {"movimientos": ["WASD", "WASD"], "golpes": ["P", "K"]},
                 "player2": {"movimientos": ["S", "D", "SA"], "golpes": ["P", "K", "INVALIDO"]}}
        result = self.utility.validar_dict(datos)
        self.assertFalse(result)

    def test_validar_dict_golpes_longitud_incorrecta(self):
        datos = {"player1": {"movimientos": ["WASD", "WASD"], "golpes": ["P", "K"]},
                 "player2": {"movimientos": ["S", "D", "SA"], "golpes": ["P", "K", "KK"]}}
        result = self.utility.validar_dict(datos)
        self.assertFalse(result)

    def test_validar_dict_golpes_caracter_invalido(self):
        datos = {"player1": {"movimientos": ["WASD", "WASD"], "golpes": ["P", "K"]},
                 "player2": {"movimientos": ["S", "D", "SA"], "golpes": ["P", "K", "INVALIDO"]}}
        result = self.utility.validar_dict(datos)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
