class Cities: # базовый класс Города
    def __init__(self, _name: str, _population: int, _size: float) -> None:

        self._name = _name
        self._population = _population
        self._size = _size

    # Атрибуты класса
    #   _name (str): Название города
    #   _population (int): Население
    #   _size (float): Площадь города


    def __str__(self) -> str:
        return f"{self._name}, {self._population} человек, {self._size} км²"

    def __repr__(self) -> str:
        return f"Наименование города: {self._name}, Население: {self._population}, Площадь города: {self._size}"

class Central_city(Cities): #дочерний класс Города в центральной России

    def __init__(self, _name: str, _population: int, _size: float, _region: str):
    """Атрибут
    _region (str): Регион нахождения
    """
        super().__init__(_name, _population, _size)
        self._region = _region


    def __str__(self) -> str:
        return f" {self._region}, {self._name}, {self._population} человек, {self._size} км²"


    def __repr__(self) -> str:
        return f"Регион: {self._region}, Наименование города: {self._name}, Население: {self._population}, Площадь города: {self._size}"

    def density(self) -> str:
        """Определение плотности населения"""
        _density = self._population / self._size
        return f"Плотность населения города {self._name} равна {_density}"

if __name__ == "__main__":
    NN_ = Cities("Нижний Новгород", "1204985", "410,68")
    Moscow_ = Central_city("Москва", "13149803", "2561,5", "Город ф.з. Москва")

    print(NN_)
    print(NN_.start())
    print(repr(NN_))

    print(Moscow_)
    print(Moscow_.start())
    print(repr(Moscow_))