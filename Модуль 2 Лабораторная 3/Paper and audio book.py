class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    @property
    def name(self) -> str:
        return self.name

    @property
    def author(self) -> str:
        return self.author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

class PaperBook:
    def __init__(self, name: str, author: str, pages: int):
        self.name = name
        self.author = author
        self.pages = pages

    @property
    def pages(self) -> int:
        return self.pages

    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int) or value <= 0:
                raise ValueError("Количество страниц не целочисленно")
        self.pages = value

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"


class AudioBook:
    def __init__(self, name: str, author: str, duration: float):
        self.name = name
        self.author = author
        self.duration = duration

    @property
    def duration(self) ->  float:
        return self.duration

    @duration.setter
    def duration(self, value: (int, float)):
        if not isinstance(value, (float, int)) or value <= 0:
            raise ValueError("Продолжительность аудиокниги должна быть вещественным положительным значением")
        self.duration = value

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"