# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Man:
    def __init__(self, height: float, age: int):
        if not isinstance(height, float):
            raise TypeError("Рост должен быть записан в метрах с точностью до десятых см")
        if height <= 0:
            raise ValueError("Рост не может быть отрицательным значением")
        self.height = height

        if not isinstance(age, int):
            raise TypeError("Возраст должен быть целым значением")
        if 0 <= age >= 150:
            raise ValueError("Значение возраста должно быть от 0 до 150 лет")
        self.age = age

    def is_height_man(self) -> bool:
        ...
# Есть ли у мужчины рост (ничего адекватного не придумала сорян)

    def growing_up(self, new_age: int) -> None:
        if not isinstance(new_age, int):
            raise TypeError("Возраст должен быть целым значением")
        if new_age < self.age:
            raise ValueError("Новый возраст не может быть меньше предыдущего")
        ...


class Persimmon:
    def __init__(self, weight: float, is_soft: bool):
        if not isinstance(is_soft, bool):
            raise TypeError("Должно принимать значение да либо нет")
        self.is_soft = is_soft

        if not isinstance(weight, (float, int)):
            raise TypeError("Вес должен принимать целое либо десятичное значение")
        if weight <= 0:
            raise ValueError("Вес хурмы должен быть положительным числом")
        self.weight = weight

    def is_persimmon_soft(self) -> bool:
        # Мягкая ли хурма
        ...

    def was_eaten(self) -> bool:
        # Сьедена ли хурма........ не пришло ничего в голову
        ...


class Organisation:
    def __init__(self, people: int, branch: int):
        if not isinstance(people, int):
            raise TypeError("Количество людей должно быть целым числом")
        if people < 1:
            raise ValueError("Количество людей не может быть меньше 1")

        if not isinstance(branch, int):
            raise TypeError("Количество филиалов должно быть целым числом")
        if branch < 0:
            raise ValueError("Количество филиалов только нулевое либо положительное число")

    def increase_people(self, new_people: int) -> None:
        if not isinstance(new_people, int):
            raise TypeError("Количество новых людей должно быть целым значением")
        if new_people < 0:
            raise ValueError("Количество новых людей не может быть отрицательным числом")

    def branch_earnings(self, money: float):
        if not isinstance(money, (int, float)):
            raise TypeError("Заработок филиала должен быть целым или десятичным значением")
        if money < 0:
            raise ValueError("Филиал не может заработать отрицательное количество денег")


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    # pass
    doctest.testmod()
