import pytest
from loops_practice import RosticsLoad

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
