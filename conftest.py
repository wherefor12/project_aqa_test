import pytest
from pages.rostics_load import RosticsLoad
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture
def rostics_monitor():
    return RosticsLoad()

@pytest.fixture
def rostics_monitor_with_yield():
    monitor = RosticsLoad()
    yield monitor
    #teardown после yield

@pytest.fixture
def page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()



