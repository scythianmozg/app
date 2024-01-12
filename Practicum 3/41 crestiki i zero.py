import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 300, 300
GRID_SIZE = 10
CELL_SIZE = WIDTH // GRID_SIZE
FPS = 30
MINE_COUNT = 15

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (192, 192, 192)

# Создание игрового поля
grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
revealed = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
mines = []

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Сапер")

# Загрузка изображений
mine_image = pygame.image.load("mine.png")
mine_image = pygame.transform.scale(mine_image, (CELL_SIZE, CELL_SIZE))

# Установка шрифта
font = pygame.font.Font(None, 36)

def draw_grid():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRAY, rect, 1)

def draw_numbers():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if revealed[row][col] and grid[row][col] > 0:
                text = font.render(str(grid[row][col]), True, BLACK)
                text_rect = text.get_rect(center=(col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2))
                screen.blit(text, text_rect)

def draw_mines():
    for row, col in mines:
        screen.blit(mine_image, (col * CELL_SIZE, row * CELL_SIZE))

def reveal_empty_cells(row, col):
    revealed[row][col] = True

    if grid[row][col] == 0:
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if 0 <= i < GRID_SIZE and 0 <= j < GRID_SIZE and not revealed[i][j]:
                    reveal_empty_cells(i, j)

def game_over():
    font_game_over = pygame.font.Font(None, 72)
    text_game_over = font_game_over.render("Game Over", True, BLACK)
    text_rect = text_game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text_game_over, text_rect)
    pygame.display.flip()
    pygame.time.delay(3000)
    pygame.quit()
    quit()

def game_won():
    font_game_won = pygame.font.Font(None, 72)
    text_game_won = font_game_won.render("You Win!", True, BLACK)
    text_rect = text_game_won.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text_game_won, text_rect)
    pygame.display.flip()
    pygame.time.delay(3000)
    pygame.quit()
    quit()

# Размещение мин на поле
mines = random.sample([(row, col) for row in range(GRID_SIZE) for col in range(GRID_SIZE)], MINE_COUNT)

# Рассчет количества мин вокруг каждой ячейки
for row in range(GRID_SIZE):
    for col in range(GRID_SIZE):
        if (row, col) not in mines:
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    if 0 <= i < GRID_SIZE and 0 <= j < GRID_SIZE and (i, j) in mines:
                        grid[row][col] += 1

# Основной игровой цикл
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            col = x // CELL_SIZE
            row = y // CELL_SIZE

            if (row, col) in mines:
                game_over()
            else:
                reveal_empty_cells(row, col)
                revealed[row][col] = True

                all_revealed = all(revealed[i][j] or (i, j) in mines for i in range(GRID_SIZE) for j in range(GRID_SIZE))
                if all_revealed:
                    game_won()

    # Отрисовка игрового поля
    screen.fill(WHITE)
    draw_grid()
    draw_numbers()
    draw_mines()
    pygame.display.flip()

    # Управление частотой кадров
    clock.tick(FPS)

# Завершение работы Pygame
pygame.quit()