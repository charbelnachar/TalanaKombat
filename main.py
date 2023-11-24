from src.modules.juego import Simulacion
from src.modules.personaje import Personaje
from src.modules.utility import Utility

# Crear una instancia de la clase Utility
utility = Utility()

# Leer datos de la pelea y las secuencias de movimientos de los personajes desde archivos JSON
data_pelea = utility.leer_json("src/recursos/ejemplo4.json")
mov_pers = utility.leer_json("src/recursos/mov_perso.json")



if  utility.validar_dict(data_pelea):
    # Crear instancias de los personajes usando los datos leídos
    tonyn = Personaje(1, "Tonyn Stallone", 6, mov_pers.get("player1"), data_pelea.get("player1"))
    arnaldor = Personaje(2, "Arnaldor Shuatseneguer", 6, mov_pers.get("player2"), data_pelea.get("player2"))

    # Imprimir una línea en blanco para mejorar la legibilidad
    print()

    # Crear una instancia de la clase Simulacion
    sim = Simulacion()

    # Determinar quién comienza la pelea
    player1, player2 = sim.definir_comienzo(tonyn, arnaldor)

    # Simular la pelea entre los dos personajes
    sim.simular_pelea(player1, player2)
