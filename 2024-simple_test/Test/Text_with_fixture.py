import pytest


@pytest.fixture
def basic_data():
    return 3, 5


def test_simple_addition(basic_data):
    assert basic_data[0] + basic_data[1] == 8


def test_simple_multiplication(basic_data):
    assert basic_data[0] * basic_data[1] == 15


some_list = [0, 7, '1', 'b']


@pytest.fixture(params=some_list)
def basic_param_data(request):
    return request.param


def test_param_data(basic_param_data):
    assert basic_param_data in some_list

# indirect fixture param


@pytest.fixture()
def negate(request):
    return -1 * request.param


@pytest.mark.parametrize("negate", [-100, 23, 0, 3.14], indirect=True)
def test_negation(negate):
    assert negate in [100, -23, 0, -3.14]


@pytest.fixture
def some_fixture():
    yield 12344

    pass


@pytest.fixture
def some_old_fixture():
    pass