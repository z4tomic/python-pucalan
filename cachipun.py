import pygame
import random
import sys

# iniciar Pygame
pygame.init()

# tamaño de ventana
WIDTH, HEIGHT = 430, 300
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ca-chi-pun')

# colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# fuentes
font = pygame.font.Font(None, 36)

# opciones de juego
options = ['piedra', 'papel', 'tijeras']

def draw_text(text, x, y):
    text_surface = font.render(text, True, BLACK)
    window.blit(text_surface, (x, y))

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Clic izquierdo
                    mouse_x, mouse_y = event.pos
                    if 50 < mouse_x < 150 and 100 < mouse_y < 150:
                        jugador = 'piedra'
                    elif 160 < mouse_x < 260 and 100 < mouse_y < 150:
                        jugador = 'papel'
                    elif 270 < mouse_x < 370 and 100 < mouse_y < 150:
                        jugador = 'tijeras'
                    else:
                        continue
                    
                    computadora = random.choice(options)
                    resultado = determinar_ganador(jugador, computadora)
                    mostrar_resultado(jugador, computadora, resultado)

        window.fill(WHITE)
        draw_text("Piedra ", 70, 110)
        draw_text("Papel ", 180, 110)
        draw_text("Tijeras", 290, 110)
        pygame.draw.rect(window, RED, (50, 100, 100, 50), 2)
        pygame.draw.rect(window, RED, (160, 100, 100, 50), 2)
        pygame.draw.rect(window, RED, (270, 100, 100, 50), 2)
        pygame.display.flip()

def determinar_ganador(jugador, computadora):
    if jugador == computadora:
        return "¡Es un empate!"
    elif (jugador == 'piedra' and computadora == 'tijeras') or \
         (jugador == 'papel' and computadora == 'piedra') or \
         (jugador == 'tijeras' and computadora == 'papel'):
        return "¡Ganaste!"
    else:
        return "¡Perdiste!"

def mostrar_resultado(jugador, computadora, resultado):
    window.fill(WHITE)
    draw_text(f"Elegiste: {jugador}", 50, 50)
    draw_text(f"La computadora eligió: {computadora}", 50, 80)
    draw_text(resultado, 50, 110)
    pygame.display.flip()
    pygame.time.delay(2000)  # Esperar 2 segundos antes de volver al menú

if __name__ == "__main__":
    main()
