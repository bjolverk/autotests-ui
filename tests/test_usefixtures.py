import pytest


@pytest.fixture
def clear_books_database() -> None:
    print("[FIXTURES] Удаляем данные из базы данных")


@pytest.fixture
def fill_books_database() -> None:
    print("[FIXTURES] Создаём новые данные в базе данных")


@pytest.mark.usefixtures('fill_books_database')
def test_read_all_books_in_library():  # (clear_books_database, fill_books_database)- так делать не стоит
    print('Read all books')


@pytest.mark.usefixtures(
    'clear_books_database',
    'fill_books_database'
)
class TestLibrary:
    def test_read_book_from_library(self):
        ...

    def test_delete_book_from_library(self):
        ...
