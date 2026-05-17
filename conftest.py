import pytest
from loops_practice import RosticsLoad


@pytest.fixture
def rostics_monitor():
    return RosticsLoad()

@pytest.fixture
def rostics_monitor_with_yield():
    monitor = RosticsLoad()
    yield monitor
    #teardown после yield