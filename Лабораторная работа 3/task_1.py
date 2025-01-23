class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name  # инициализируем защищенный атрибут
        self._author = author  # инициализируем защищенный атрибут

    @property
    def name(self):
        return self._name  # внутри класса обращаемся к защищенному атрибуту

    @property
    def author(self):
        return self._author  # внутри класса обращаемся к защищенному атрибуту

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)  # наследуем
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter  # свойство с проверками при присвоении им значений
    def pages(self, pages: int) -> None:
        if not isinstance(pages, int):
            raise TypeError
        if not 0 <= pages:
            raise ValueError
        self._pages = pages

    def __str__(self):
        return f"Бумажная книга {self.name}. Автор {self.author}"  # перегружаем

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)  # наследуем
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter  # свойство с проверками при присвоении им значений
    def duration(self, duration: float) -> None:
        if not isinstance(duration, float):
            raise TypeError
        if not 0 <= duration:
            raise ValueError
        self._duration = duration

    def __str__(self):
        return f"Аудио книга {self.name}. Автор {self.author}"  # перегружаем

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
