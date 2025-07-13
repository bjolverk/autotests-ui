import pytest
from _pytest.fixtures import SubRequest


# 1, 2, 3, -1

@pytest.mark.parametrize('number', [1, 2, 3, -1])
def test_numbers(number: int):
    assert number > 0


@pytest.mark.parametrize('number, expected', [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected


@pytest.mark.parametrize('browser', ['Chromium', 'Webkit', 'Firefox'])
@pytest.mark.parametrize('os', ['macOS', 'Windows', 'Linux', 'Debian'])
def test_multiplication_of_numbers(os: str, browser: str):
    assert len(os + browser) > 0


@pytest.fixture(params=["chromium", "webkit", "firefox"])
# Фикстура будет возвращать три разных браузера
# Соотвественно все автотесты использующие данную фикстуру будут запускаться три раза
def browser(request: SubRequest) -> str:
    return request.param  # Внутри атрибута param находится одно из значений "chromium", "webkit", "firefox"


# В самом автотесте уже не нужно добавлять параметризацию, он будет автоматически параметризован из фикстуры
def test_open_browser(browser: str):
    # Используем фикстуру в автотесте, она вернет нам браузер в виде строки
    print(f"Running test on browser: {browser}")


@pytest.mark.parametrize('user', ['Alice', 'Zara'])
class TestOperations:

    @pytest.mark.parametrize('account', ['Credit Card', 'Debit Card'])
    def test_user_with_operations(self, user: str, account: str):
        print(f'User with operations {user}')

    def test_user_without_operations(self, user: str):
        print(f'User without operations {user}')


users = {
    '+70000000011': 'User with money on bank account',
    '+70000000022': 'User without money on bank account',
    '+70000000033': 'User with operations on bank account'
}


# @pytest.mark.parametrize(
#     'phone_number',
#     ['+70000000011', '+70000000022', '+70000000033'],
#     ids=[
#         'User with money on bank account',
#         'User without money on bank account',
#         'User with operations on bank account',
#     ]
# )
@pytest.mark.parametrize(
    'phone_number',
    users.keys(),
    ids=lambda phone_number: f'{phone_number} : {users[phone_number]}'
)
def test_identification(phone_number: str):
    pass
