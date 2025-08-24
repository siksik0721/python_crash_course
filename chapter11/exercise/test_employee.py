import pytest
from employee import Employee


@pytest.fixture
def employee_fixture():
    emp = Employee("철수", "김", 10000)
    return emp


def test_give_default_raise(employee_fixture):
    employee_fixture.give_raise()
    assert 15000 == employee_fixture.salary


def test_give_custom_raise(employee_fixture):
    employee_fixture.give_raise(10000)
    assert 20000 == employee_fixture.salary
