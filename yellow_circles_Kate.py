import pygame

WIDTH = 1000  # ширина игрового окна
HEIGHT = 500  # высота игрового окна
FPS = 50  # ч
# частота кадров в секунду
YELLOW = pygame.Color('yellow')
BlUE = pygame.Color('blue')


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.r = 1
        self.k = 0
        self.pos = pos
        self.image = pygame.Surface([self.r, self.r])
        self.image.fill(BlUE)
        self.image.set_colorkey(BlUE)
        self.color = YELLOW
        pygame.draw.circle(self.image, self.color, (self.r, self.r), self.r, 0)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self):
        pygame.draw.circle(self.image, self.color, (self.r, self.r), self.r, 0)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.r += 1
        self.image = pygame.Surface([self.r, self.r])

def main():
    pygame.init()
    pygame.mixer.init()  # для звука

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()
    screen.fill(BlUE)
    all_sprites = pygame.sprite.Group()
    running = True

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                player = Player(event.pos, (WIDTH, HEIGHT))
                all_sprites.add(player)

        all_sprites.update()

        # Рендеринг
        screen.fill(BlUE)
        all_sprites.draw(screen)
        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()

    pygame.quit()


main()