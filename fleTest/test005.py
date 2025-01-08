from PIL import Image, ImageTk
import os
import time
import tkinter as tk


class ImageSlideshow:
    def __init__(self, root):
        self.root = root
        self.images_path = "pictures"
        self.image_files = []
        self.current_image_index = 0
        self.image_label = None
        self.text_label = None

        # Получаем список файлов из папки "pictures"
        self.get_image_files()

        # Создаем главное окно и устанавливаем его на полный экран
        self.root.attributes('-fullscreen', True)

        # Создаем метку для отображения изображений
        self.image_label = tk.Label(self.root)
        self.image_label.pack(fill=tk.BOTH, expand=True)

        # Создаем метку для отображения текста
        self.text_label = tk.Label(self.root, text="", font=('Arial', 24), bg='black', fg='white', highlightthickness=0, borderwidth=0)
        self.text_label.pack(side=tk.BOTTOM, fill=tk.X)

        # Запускаем слайдшоу
        self.start_slideshow()

    def get_image_files(self):
        # Получаем список файлов из папки "pictures"
        for filename in os.listdir(self.images_path):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                self.image_files.append(os.path.join(self.images_path, filename))

    def start_slideshow(self):
        # Проверяем, есть ли изображения в папке
        if not self.image_files:
            print("No images found in the 'pictures' folder.")
            self.root.destroy()
            return

        # Отображаем первое изображение
        self.display_image()

        # Запускаем цикл показа изображений с интервалом 30 секунд
        self.root.after(30000, self.next_image)

    def display_image(self):
        # Открываем изображение с помощью PIL
        image = Image.open(self.image_files[self.current_image_index])

        # Получаем размеры экрана
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Масштабируем изображение под размеры экрана
        image = image.resize((screen_width, screen_height), Image.LANCZOS)

        # Создаем объект ImageTk для отображения изображения в Tkinter
        image_tk = ImageTk.PhotoImage(image)

        # Устанавливаем изображение в метку
        self.image_label.configure(image=image_tk)
        self.image_label.image = image_tk

        # Получаем название файла без расширения
        filename = os.path.basename(self.image_files[self.current_image_index])
        filename = os.path.splitext(filename)[0]

        # Устанавливаем текст для бегущей строки
        self.text_label.configure(text=filename)

        # Применяем эффекты прозрачности и анимации к тексту
        self.apply_text_effects()

    def apply_text_effects(self):
        # Создаем анимацию для плавного движения текста
        self.text_label.place(x=self.root.winfo_screenwidth(), y=int(self.root.winfo_screenheight() / 2) - 20)
        self.text_label.update()
        text_width = self.text_label.winfo_width()
        animation_duration = 100_000  # Длительность анимации в миллисекундах
        distance = text_width + self.root.winfo_screenwidth()

        # Запускаем анимацию
        self.animate_text(text_width, distance, animation_duration)

    def animate_text(self, width, distance, duration):
        start_time = time.time()

        def animate():
            nonlocal start_time
            elapsed_time = time.time() - start_time
            if elapsed_time > duration / 1000:
                self.next_image()
                return

            x_offset = int(distance * (1 - elapsed_time / (duration / 1000)))
            y_offset = int(self.root.winfo_screenheight() / 2) - 20
            self.text_label.place(x=x_offset, y=y_offset)

            self.root.after(50, animate)

        animate()

    def next_image(self):
        # Увеличиваем индекс текущего изображения
        self.current_image_index += 1

        # Если достигнут конец списка изображений, возвращаемся к первому изображению
        if self.current_image_index == len(self.image_files):
            self.current_image_index = 0

        # Отображаем следующее изображение
        self.display_image()

        # Запускаем таймер для показа следующего изображения через 30 секунд
        self.root.after(30000, self.next_image)


root = tk.Tk()
app = ImageSlideshow(root)
root.mainloop()
