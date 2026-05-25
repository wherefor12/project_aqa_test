import pytest
from pages.rostics_load import RosticsLoad
from pages.practice import Practice
from pages.login_page import LoginPage


def test_sum():
    assert 2 + 2 == 4


@pytest.mark.smoke
def test_monitor_load(rostics_monitor):
    loads = rostics_monitor.monitor_load()
    assert len(loads) == 10


def test_monitor_load_values_are_in_range(rostics_monitor):
    loads = rostics_monitor.monitor_load()
    assert all(0 <= load <= 100 for load in loads)


@pytest.mark.parametrize(
        "loads, results", 
        [
            (0, True),
            (50, True),
            (120, False),
        ],
)   

def test_load(loads, results):
    is_range = 0 <= loads and loads <= 100
    assert is_range == results


def test_login_success():
    driver = object()
    page = LoginPage(driver)

    page.open_page()
    page.login("user", "pass")

    assert page.login_in == True

def test_open_browser(page):
    page.goto("https://www.google.com")