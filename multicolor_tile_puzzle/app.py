import pygame

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
cell_size = 50  # Tamaño de cada celda
cols = 14       # Número de columnas
rows = 4        # Número de filas
screen_width = cols * cell_size
screen_height = rows * cell_size
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jugador en la Matriz con Celdas Coloreadas")

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Posición inicial del jugador (columna, fila)
player_pos = [0, 0]

# Celdas coloreadas (diccionario de coordenadas y colores)
colored_cells = {
    (2, 1): GREEN,
    (5, 2): RED,
    (10, 0): GREEN,
    (12, 3): RED,
}

# Control del juego
running = True
while running:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Movimiento del jugador
            if event.key == pygame.K_LEFT and player_pos[0] > 0:
                player_pos[0] -= 1
            elif event.key == pygame.K_RIGHT and player_pos[0] < cols - 1:
                player_pos[0] += 1
            elif event.key == pygame.K_UP and player_pos[1] > 0:
                player_pos[1] -= 1
            elif event.key == pygame.K_DOWN and player_pos[1] < rows - 1:
                player_pos[1] += 1

    # Dibujar en la pantalla
    screen.fill(BLACK)

    # Dibujar la cuadrícula y colorear celdas específicas
    for row in range(rows):
        for col in range(cols):
            rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
            # Verificar si la celda tiene un color específico
            if (col, row) in colored_cells:
                pygame.draw.rect(screen, colored_cells[(col, row)], rect)
            else:
                pygame.draw.rect(screen, WHITE, rect, 1)

    # Dibujar al jugador
    # Dibujar al jugador centrado en la celda
    player_rect = pygame.Rect(
        player_pos[0] * cell_size + cell_size // 4,
        player_pos[1] * cell_size + cell_size // 4,
        cell_size // 2,
        cell_size // 2
    )
    pygame.draw.rect(screen, BLUE, player_rect)


    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
