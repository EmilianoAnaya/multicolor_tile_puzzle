from enum import Enum

# Ruta de canciones
class Songs(Enum):
    MAIN_THEME = "multicolor_tile_puzzle/resources/oh-dungeon.mp3"
    VICTORY_THEME = "multicolor_tile_puzzle/resources/Hyes_short.wav"

# Color de jugador
PLAYER_COLOR = (255,255,255)

# Colores de celdas
ROSA = (255, 1, 237)
ROJO = (255, 0, 0)
VERDE = (71, 211, 89)
AMARILLO = (255, 192, 0)
AZUL = (0, 112, 192)
MORADO = (112, 48, 160)

# CELDAS COLOREADAS
CELLS_COLORS = {
    (0, 0): ROJO,
    (0, 1): ROSA,
    (0, 2): ROSA,
    (0, 3): ROJO,

    (1,0):AMARILLO,
    (1,1):ROSA,
    (1,2):ROSA,
    (1,3):AMARILLO,

    (2,0):ROSA,
    (2,1):ROJO,
    (2,2):ROJO,
    (2,3):MORADO,

    (3,0):AZUL,
    (3,1):ROSA,
    (3,2):ROJO,
    (3,3):AZUL,

    (4,0):ROJO,
    (4,1):ROSA,
    (4,2):MORADO,
    (4,3):AMARILLO,

    (5,0):VERDE,
    (5,1):ROJO,
    (5,2):ROSA,
    (5,3):ROJO,

    (6,0):ROJO,
    (6,1):MORADO,
    (6,2):AZUL,
    (6,3):ROSA,

    (7,0):ROJO,
    (7,1):AMARILLO,
    (7,2):ROSA,
    (7,3):MORADO,

    (8,0):ROJO,
    (8,1):AZUL,
    (8,2):ROJO,
    (8,3):MORADO,

    (9,0):ROSA,
    (9,1):AMARILLO,
    (9,2):AZUL,
    (9,3):ROJO,

    (10,0):AZUL,
    (10,1):ROJO,
    (10,2):ROJO,
    (10,3):ROJO,

    (11,0):AMARILLO,
    (11,1):MORADO,
    (11,2):AZUL,
    (11,3):MORADO,

    (12,0):ROJO,
    (12,1):ROJO,
    (12,2):ROSA,
    (12,3):ROJO,

    (13,0):VERDE,
    (13,1):AMARILLO,
    (13,2):MORADO,
    (13,3):AMARILLO,
}   