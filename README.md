

# Desafío Talana Kombat JRPG

### Descripción del Desafío
¡Hola Querid@ Candidat@! A continuación, te presentamos el siguiente desafío para postular al puesto de desarrollador@ Software Developer Engineer. Te invitamos a hacer tu mejor esfuerzo, no importa si no terminas y solo lo resuelves parcialmente, desde ya te agradecemos por participar.

### Evaluación
No sólo evaluamos algoritmos, también buenas prácticas de arquitectura, limpieza de código, estructura del proyecto, y en general cómo dejas tu marca de seniority en la entrega, por lo que te recomendamos que hagas tu mejor esfuerzo.

### Duración y en qué consiste la prueba
- 48 horas (Si terminas antes mejor, pero si necesita más tiempo, dale, nos enfocamos más en una prueba orientada a resultados a que solo medir el tiempo)
- Deberás desarrollar una solución que relate la pelea y diga el resultado final.
- Deberás responder unas preguntas para conocerte un poco más

### Forma de entrega
El proyecto deberá estar en un repositorio compartido. Si lo entregas en docker mucho mejor.

### Lenguajes, frameworks y herramientas
Usa el lenguaje que más te acomode (Si usas Python, mucho mejor, también nos gusta Go).

### Ejercicio Talana Kombat JRPG
Talana Kombat es un juego donde 2 personajes se enfrentan hasta la muerte. Cada personaje tiene 2 golpes especiales que se ejecutan con una combinación de movimientos + 1 botón de golpe. Los botones que se usan son (W)Arriba, (S)Abajo, (A)Izquierda, (D)Derecha, (P)Puño, (K)Patada.

#### Golpes de Nuestros Personajes
- **Tonyn Stallone:**
  - Combinación: DSD + P
  - Energía que quita: 3
  - Nombre del movimiento: Taladoken

  - Combinación: SD + K
  - Energía que quita: 2
  - Nombre del movimiento: Remuyuken

  - Combinación: P o K
  - Energía que quita: 1
  - Nombre del movimiento: Puño o Patada

- **Arnaldor Shuatseneguer:**
  - Combinación: SA + K
  - Energía que quita: 3
  - Nombre del movimiento: Remuyuken

  - Combinación: ASA + P
  - Energía que quita: 2
  - Nombre del movimiento: Taladoken

  - Combinación: P o K
  - Energía que quita: 1
  - Nombre del movimiento: Puño o Patada

#### Información Importante
- Parte atacando el jugador que envió una combinación menor de botones (movimiento + golpes).
- En caso de empate, parte el con menos movimientos, si empatan de nuevo, inicia el con menos golpes, si hay empate de nuevo, inicia el player 1 (total el player 2 siempre es del hermano chico).
- La secuencia completa del combate de cada jugador se entrega de una vez (consolidada en un JSON).
- Cada personaje tiene 6 Puntos de energía.
- Un personaje muere cuando su energía llega a 0 y de inmediato finaliza la pelea.
- Tony es el player 1, siempre ataca hacia la derecha (y no cambia de lado).
- Arnaldor es el player 2, siempre ataca hacia la izquierda (y no cambia de lado).
- Los personajes se atacan uno a la vez estilo JRPG, por turnos hasta que uno es derrotado, los golpes no pueden ser bloqueados, se asume que siempre son efectivos.

#### Datos de Entrada
Los datos llegan como un JSON con botones de movimiento y golpe que se correlacionan para cada jugada. Los movimientos pueden ser un string de largo máximo 5 (puede ser vacío), y los golpes pueden ser un solo botón máximo (puede ser vacío). Se asume que el botón de golpe es justo después de la secuencia de movimiento, es decir, AADSD + P es un Taladoken (antes se movió para atrás 2 veces); DSDAA + P son movimientos más un puño.

### Desarrollo de la Solución
Desarrolla una solución que relate la pelea e informe el resultado final. Asegúrate de seguir las condiciones y restricciones del desafío.

### Archivos Ejemplos
  - [ejemplo1.json] comienza Player1 y gana Tony
  - [ejemplo2.json] comienza Player2 y gana Arnaldor
  - [ejemplo3.json] Empatan
  - [ejemplo4.json] Error en formato
### Ejecución
```bash
python main.py
```

### Ejecución de las pruebas 
```bash
python -m unittest discover -s test -p "test_*.py"
```



