import pytest
from pages.rostics_load import RosticsLoad


@pytest.fixture
def rostics_monitor():
    return RosticsLoad()

@pytest.fixture
def rostics_monitor_with_yield():
    monitor = RosticsLoad()
    yield monitor
    #teardown после yield



