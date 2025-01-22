BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, _id: int, _name: str, _pages: int):
        self.attr1 = _id
        self.attr2 = _name
        self.attr3 = _pages

    def __str__(self):
        return f'Книга "{self.attr2}"'
    def __repr__(self):
        return f"Book(id_={self.attr1}, name='{self.attr2}', pages={self.attr3})"

if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(_id=book_dict["id"], _name=book_dict["name"], _pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
