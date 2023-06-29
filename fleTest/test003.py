import pygame
import time

# Инициализация Pygame
pygame.init()

# Загрузка изображения
image_path = "01.jpg"
image = pygame.image.load(image_path)

# Получение размеров экрана
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

# Создание окна с размерами экрана
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

# Получение размеров изображения
image_width = image.get_width()
image_height = image.get_height()

# Масштабирование изображения до размеров экрана
scaled_image = pygame.transform.scale(image, (screen_width, screen_height))

# Определение параметров бегущей строки
text = "Running Text Example"
font = pygame.font.Font(None, 36)
text_color = (255, 255, 255)

# Получение размеров текста
text_width, text_height = font.size(text)

# Создание поверхности для текста с прозрачным фоном
text_surface = font.render(text, True, text_color)
text_surface.set_alpha(128)  # Установка прозрачности (значение альфа-канала от 0 до 255)

# Определение начальных координат бегущей строки
x_pos = screen_width
y_pos = 20

# Основной цикл игры
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q and pygame.key.get_mods() & pygame.KMOD_CTRL:
                running = False

    # Масштабирование изображения в зависимости от размера экрана
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    scaled_image = pygame.transform.scale(image, (screen_width, screen_height))

    # Вывод изображения на экран
    screen.blit(scaled_image, (0, 0))

    # Отображение бегущей строки
    screen.blit(text_surface, (x_pos, y_pos))
    x_pos -= 1  # Изменение горизонтальной позиции для создания эффекта бегущей строки
    if x_pos < -text_width:
        x_pos = screen_width  # Возвращение бегущей строки в начальную позицию

    pygame.display.update()
    pygame.time.delay(10)  # Задержка для контроля скорости бегущей строки

# Завершение работы Pygame
pygame.quit()
