import pygame

# Определяем константы для ширины, высоты и частоты кадров в секунду
WIDTH = 1000
HEIGHT = 500
FPS = 10

# Определяем цвета, которые будут использоваться в игре
YELLOW = pygame.Color('yellow')
BLUE = pygame.Color('blue')


# Создаем класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self, size):
        # Вызов конструктора родительского класса (Sprite)
        super().__init__()

        # Определяем радиус и положение круга
        self.r = 10
        self.pos = None

        # Создаем поверхность, на которой будет отрисовываться круг
        self.image = pygame.Surface(size)

        # Заливка поверхности синим цветом
        self.image.fill(BLUE)

        # Установка цвета-контура, чтобы круг не имел видимого границы
        self.image.set_colorkey(BLUE)

        # Определяем цвет, который будет использоваться для рисования круга
        self.color = YELLOW

        # Получаем прямоугольник, который ограничивает изображение
        self.rect = self.image.get_rect()

    # Метод для установки центра круга
    def set_center(self, pos):
        self.pos = pos
        self.r = 10  # Начальный радиус круга
        self.image.fill(BLUE)  # Очистка поверхности

    # Метод для обновления круга на поверхности
    def update(self):
        if self.pos is None:
            return
        # Рисуем круг на поверхности, используя заданные параметры
        pygame.draw.circle(self.image, self.color, self.pos, self.r, self.r)
        self.r += 1


def main():
    # Инициализируем pygame
    pygame.init()

    # Создаем окно с заданными размерами
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Устанавливаем заголовок окна
    pygame.display.set_caption("Желтый круг")

    # Создаем объект Clock для контроля скорости кадров
    clock = pygame.time.Clock()

    # Создаем группу спрайтов, в которую будем добавлять игрока
    all_sprites = pygame.sprite.Group()

    # Создаем объект игрока
    player = Player((WIDTH, HEIGHT))

    # Добавляем игрока в группу спрайтов
    all_sprites.add(player)

    # Устанавливаем переменную running в значение True, чтобы запустить игру
    running = True

    # Основной игровой цикл
    while running:
        # Ограничиваем скорость кадров до FPS
        clock.tick(FPS)

        # Обрабатываем все события, которые произошли с pygame
        for event in pygame.event.get():
            # Обработка события закрытия окна
            if event.type == pygame.QUIT:
                running = False

            # Обработка события нажатия кнопки мыши
            if event.type == pygame.MOUSEBUTTONDOWN:
                player.set_center(event.pos)

            # Обновляем все спрайты
        all_sprites.update()

        # Заполняем экран синим цветом
        screen.fill(BLUE)

        # Отрисовываем все спрайты на экране
        all_sprites.draw(screen)

        # Переворачиваем экран, чтобы все отрисованные объекты стали видимыми
        pygame.display.flip()

        # Когда игровой цикл завершается, мы выходим из pygame
    pygame.quit()


if __name__ == '__main__':
    main()
