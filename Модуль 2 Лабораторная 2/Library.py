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

# TODO написать класс Library
class Library:
    def __init__(self, books: int):
        if books is None:
            self.books = ()
        else:
            self.books = books

    def __get_next_book_id__(self):
        if not self.books:
            return 1
        else:
            return self.books + 1

    def __get_index_by_book_id__(self, _id):
        for i, books in enumerate(self.books):
            if books.id == _id:
                return i
            raise ValueError ("Книги с запрашиваемым id не существует")

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(_id=book_dict["id"], _name=book_dict["name"], _pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
