import doctest

# TODO Написать 3 класса с документацией и аннотацией типов

class Bookshelf:
    def __init__(self, free_space: int, occupied_place: int):
        """
        Создание и подготовка к работе объекта "Книжная полка"

        :param free_space: Свободное место
        :param occupied_place: Занятое место книгами

        Примеры:
        >>> bookshelf = Bookshelf(10, 0) # инициализация экземпляра класса
        """
        if not isinstance(free_space, (int)):
            raise TypeError("Свободное место должно быть int")
        if free_space <= 0:
            raise ValueError("Свободное место должно быть положительным числом")
        self.free_space = free_space


        if not isinstance(occupied_place, (int)):
            raise TypeError("Занятое место должно быть int")
        if occupied_place < 0:
            raise ValueError("Занятое место должно быть положительным числом")
        self.free_space = free_space

    def is_empty_bookshelf(self):
        """
        Функция проверяет пустая ли полка

        :return: Является ли полка пустой

        Примеры:
        >>> bookshelf = Bookshelf(10, 0)
        >>> bookshelf.is_empty_bookshelf()
        """
        ...

    def add_book_to_bookshelf(self, book: int):
        """
        Добавление книги на книжную полку
        :param book: Количество добавляемых книг

        :raise ValueError: Если количество добавляемых книг превышает свободное место на полке, то вызвать ошибку

        :return: Количество добавленных книг
        Примеры:
        >>> bookshelf = Bookshelf(10, 0)
        >>> bookshelf.add_book_to_bookshelf(5)
        """
        if not isinstance(book, (int)):
            raise TypeError("Добавляемые книги должны быть int")
        if book < 0:
            raise ValueError("Добавляемые книги должны быть положительным числом")
        ...

    def remove_book_from_bookshelf(self, extractable_book: int):
        """
        Извлечение книги с книжной полки
        :param extractable_book: Количество извлекаемых книг

        :raise ValueError: Если количество извлекаемых книг превышает количество книг, находящихся на полке, то вызвать ошибку

        :return: Количество извлеченных книг
        Примеры:
        >>> bookshelf = Bookshelf(10, 5)
        >>> bookshelf.remove_book_from_bookshelf(2)
        """
        ...

class Car:
    def __init__(self, max_speed: float, fact_speed: float):
        """
        Создание и подготовка к работе объекта "Машина"

        :param max_speed: Максимальная скорость в километрах в час
        :param fact_speed: Фактическая скорость в километрах в час

        Примеры:
        >>> car = Car(300, 0) # инициализация экземпляра класса
        """
        if not isinstance(max_speed, (int, float)):
            raise TypeError("Максимальная скорость должна быть int или float")
        if max_speed <= 0:
            raise ValueError("Максимальная скорость должна быть положительным числом")
        self.max_speed = max_speed


        if not isinstance(fact_speed, (int, float)):
            raise TypeError("Факстическая скорость должна быть int или float")
        if fact_speed < 0:
            raise ValueError("Фактическая скорость должна быть положительным числом")
        self.fact_speed = fact_speed

    def is_car_coming(self):
        """
        Функция проверяет едет ли машина

        :return: Является ли машина движущейся

        Примеры:
        >>> car = Car(300, 0)
        >>> car.is_car_coming()
        """
        ...

    def speed_up_car(self, speed_up: int, float):
        """
        Прибавление скорости
        :param speed_up: Количество прибавляемых километров в час

        :raise ValueError: Если количество добавляемых километров в час превышает максимальную скорость, то вызвать ошибку

        :return: Количество добавленных километров в час
        Примеры:
        >>> car = Car(300, 0)
        >>> car.speed_up_car(100)
        """
        if not isinstance(speed_up, (int, float)):
            raise TypeError("Добавляемые километры в час должны быть int или float")
        if speed_up < 0:
            raise ValueError("Добавляемые километры в час должны быть положительным числом")
        ...

    def speed_down_car(self, speed_down: int, float):
        """
        Убавление скорости
        :param speed_down: Количество убавляемых километров в час

        :raise ValueError: Если количество убавляемых километров в час превышает количество километров в час, с которой едет машина, то вызвать ошибку

        :return: Количество убавляемых километров в час
        Примеры:
        >>> car = Car(300, 100)
        >>> car.speed_down_car(50)
        """
        ...

class Elevator:
    def __init__(self, max_load: float, fact_load: float):
        """
        Создание и подготовка к работе объекта "Лифт"

        :param max_load: Максимальная загрузка в кг
        :param fact_load: Факстическая загрузка в кг

        Примеры:
        >>> elevator = Elevator(300, 0) # инициализация экземпляра класса
        """
        if not isinstance(max_load, (int, float)):
            raise TypeError("Максимальная загрузка должна быть int или float")
        if max_load <= 0:
            raise ValueError("Максимальная загрузка должна быть положительным числом")
        self.max_load = max_load


        if not isinstance(fact_load, (int, float)):
            raise TypeError("Факстическая загрузка должна быть int или float")
        if fact_load < 0:
            raise ValueError("Фактическая загрузка должна быть положительным числом")
        self.fact_load = fact_load

    def is_empty_elevator(self):
        """
        Функция проверяет пустой ли лифт

        :return: Является ли лифт пустой

        Примеры:
        >>> elevator = Elevator(300, 0)
        >>> elevator.is_empty_elevator()
        """
        ...

    def is_able_lift_weight(self):
        """
        Функция проверяет сможет ли поднять лифт вес

        :return: Сможет ли поднять такой вес
        Примеры:
        >>> elevator = Elevator(300, 200)
        >>> elevator.is_able_lift_weight()
        """
        ...

if __name__ == "__main__":
    doctest.testmod() # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
