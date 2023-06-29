import pygame
import time
import os

# Инициализация Pygame
pygame.init()

# Получение размеров экрана
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

# Создание окна с размерами экрана
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

# Получение списка файлов в папке с фотографиями
photos_folder = "pictures"
photos = os.listdir(photos_folder)

# Определение параметров бегущей строки
font = pygame.font.Font(None, 150)
text_color = (255, 255, 255)

# Определение начальных координат бегущей строки
x_pos = screen_width
y_pos = 20

# Определение времени отображения каждого изображения (в секундах)
display_time = 30
start_time = time.time()

# Определение скорости движения текста
text_speed = 5

clock = pygame.time.Clock()  # Создание объекта Clock для контроля обновления кадров

# Основной цикл игры
running = True
photo_index = 0  # Индекс текущей отображаемой фотографии
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Загрузка текущей фотографии
    current_photo = pygame.image.load(os.path.join(photos_folder, photos[photo_index]))
    photo_width = current_photo.get_width()
    photo_height = current_photo.get_height()

    # Масштабирование фотографии до размеров экрана
    scaled_photo = pygame.transform.scale(current_photo, (screen_width, screen_height))

    # Вывод фотографии на экран
    screen.blit(scaled_photo, (0, 0))

    # Получение текущего наименования фотографии
    photo_name = os.path.splitext(photos[photo_index])[0]

    # Создание поверхности для текста с прозрачным фоном
    text_surface = font.render(photo_name, True, text_color)
    text_width, text_height = font.size(photo_name)

    # Определение текущей позиции текста с помощью интерполяции
    target_x = -text_width
    x_pos = pygame.lerp(x_pos, target_x, 0.05)

    # Отображение бегущей строки
    screen.blit(text_surface, (x_pos, y_pos))

    pygame.display.update()
    clock.tick(60)  # Ограничение обновления кадров до 60 кадров в секунду

    # Переключение на следующую фотографию
    elapsed_time = time.time() - start_time
    if elapsed_time >= display_time:
        photo_index = (photo_index + 1) % len(photos)
        start_time = time.time()

# Завершение работы Pygame
pygame.quit()
