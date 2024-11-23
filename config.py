import pygame
import random


WIDTH, HEIGHT = 300, 600
BLOCK_SIZE = 30


COLORS = [
    (0, 0, 0),  
    (255, 0, 0),  
    (0, 255, 0),  
    (0, 0, 255),  
    (255, 255, 0),  
]

SHAPES = [
    [[1, 1, 1, 1]],  
    [[1, 1], [1, 1]],  
    [[0, 1, 0], [1, 1, 1]],  
    [[1, 1, 0], [0, 1, 1]],  
    [[0, 1, 1], [1, 1, 0]],  
]

class Tetris:
    def __init__(self):
        self.board = [[0] * (WIDTH // BLOCK_SIZE) for _ in range(HEIGHT // BLOCK_SIZE)]
        self.current_piece = self.new_piece()

    def new_piece(self):
        shape = random.choice(SHAPES)
        return shape

    def draw_board(self, screen):
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                color = COLORS[self.board[y][x]]
                pygame.draw.rect(screen, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    game = Tetris()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill((255, 255, 255))  
        game.draw_board(screen)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()