import pygame
from constants import CELLS_COLORS, PLAYER_COLOR, Songs
from states import STATES

# Inicializar Pygame
pygame.init()
pygame.mixer.init()

# Configuración de la pantalla
cell_size = 50  # Tamaño de cada celda
cols = 14       # Número de columnas
rows = 4        # Número de filas
screen_width = cols * cell_size
screen_height = rows * cell_size
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jugador en la Matriz con Celdas Coloreadas")
actual_state = 0
player_pos = [0, 1] # Posición inicial del jugador (columna, fila)

# Controlar la música del juego
pygame.mixer.music.load(Songs.MAIN_THEME)
pygame.mixer.music.play()


# Control del juego
running = True
while running:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            # Movimiento del jugador
            if event.key == pygame.K_LEFT:
                actual_state = STATES[actual_state][1]
                player_pos[0] = STATES[actual_state][0][0] 
                player_pos[1] = STATES[actual_state][0][1] 

            elif event.key == pygame.K_RIGHT:
                actual_state = STATES[actual_state][2]
                player_pos[0] = STATES[actual_state][0][0] 
                player_pos[1] = STATES[actual_state][0][1] 

            elif event.key == pygame.K_UP:
                actual_state = STATES[actual_state][3]
                player_pos[0] = STATES[actual_state][0][0] 
                player_pos[1] = STATES[actual_state][0][1] 

            elif event.key == pygame.K_DOWN:
                actual_state = STATES[actual_state][4]
                player_pos[0] = STATES[actual_state][0][0] 
                player_pos[1] = STATES[actual_state][0][1]

        elif STATES[actual_state] == 32:
            pygame.mixer.music.stop() 

    # Dibujar en la pantalla
    for row in range(rows):
        for col in range(cols):
            rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
            # Verificar si la celda tiene un color específico
            pygame.draw.rect(screen, CELLS_COLORS[(col, row)], rect)

    # Dibujar al jugador centrado en la celda
    player_rect = pygame.Rect(
        player_pos[0] * cell_size + cell_size // 4,
        player_pos[1] * cell_size + cell_size // 4,
        cell_size // 2,
        cell_size // 2
    )
    pygame.draw.rect(screen, PLAYER_COLOR, player_rect)


    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
