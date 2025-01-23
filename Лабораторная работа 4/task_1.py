if __name__ == "__main__":
    class Automobile:
        """ Базовый класс автомобиль. Есть два типа автомобилей - с бензиновым и электродвигателем.
        Для всех типов хранения есть:
        - марка (brand)
        - модель (model)
        - запас хода (range)
        У бензиновых авто есть количество бензина (fuel), как числа с плавающей запятой.
        У электромобилей есть количество заряда (charging) целочисленного типа.

        Метод __str__ наследуется в дочерних классах. Метод __repr__ перегружается."""

        def __init__(self, brand: str, model: str, range: int):
            self._brand = brand
            self._model = model
            self._range = range

        @property
        def brand(self):
            return self._brand  # не могут изменяться, поэтому делаю непубличными

        @property
        def model(self):
            return self._model  # не могут изменяться, поэтому делаю непубличными

        @property
        def range(self):
            return self._range  # не могут изменяться, поэтому делаю непубличными

        def __str__(self) -> str:
            return f"Марка автомобиля {self.brand}. Модель автомобиля {self.model}"

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r})"

        def is_battery_low(self) -> str:
            """Проверяет, находится ли запас хода выше нормы (к примеру, больше 50 км) .
            Если нет, то просит заехать на колонку. Этот метод наследуется в дочерних классах."""
            return f"{self.brand} {self.model} {self.range} заедьте на колонку."

        def get_fuel_or_charge(self) -> str:
            """Данный метод просит заправщика заправить или зарядить авто.
            Этот метод перегружается в дочерних классах."""
            return f"{self.brand} {self.model} {self.range}"

    class PetrolEngine(Automobile):
        """ Дочерний класс автомобиль с обычным двигателем. """

        def __init__(self, brand: str, model: str, range: int, fuel: float):
            super().__init__(brand, model, range)
            self.fuel = fuel  # дополнительный параметр

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, fuel={self.fuel!r})"

        def get_fuel_or_charge(self) -> str:
            """Перегружается. Т.к. просит заправщика заправить бензин."""
            return f"{self.brand} {self.model} {self.range} {self.fuel} заправьте бензин."

    class ElectroEngine(Automobile):
        """ Дочерний класс автомобиль с электродвигателем. """

        def __init__(self, brand: str, model: str, range: int, charging: int):
            super().__init__(brand, model, range)
            self.charging = charging  # дополнительный параметр

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, charging={self.charging!r})"

        def get_fuel_or_charge(self) -> str:
            """Перегружается. Т.к. просит заправщика поставить на зарядку."""
            return f"{self.brand} {self.model} {self.range} {self.charging} поставьте на зарядку."
    pass
