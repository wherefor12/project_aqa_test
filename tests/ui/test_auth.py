import os
import pytest
from playwright.sync_api import expect
from pages.auth_pages import LOGIN_URL, HOME_URL, ERROR_URL
from pages.auth_pages import AuthPage
import dotenv




@pytest.mark.ui
def test_successful(page):
    username = os.getenv("GH_USER")
    password = os.getenv("GH_PASS")

    if not username or not password:
        pytest.skip("Нет переменных GH_USER / GH_PASS")
    
    login = AuthPage(page)
    login.open()
    login.login(username, password)
    expect(page).to_have_url(HOME_URL)


@pytest.mark.ui
def test_failed(page):
    username = "1234"
    password = "5678"

    login = AuthPage(page)
    login.open()
    login.login(username, password)
    expect(page).to_have_url(ERROR_URL)

    error_massage = page.locator("#js-flash-container")
    expect(error_massage).to_be_visible()
