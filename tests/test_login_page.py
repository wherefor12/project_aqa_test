class BasePage:
    def __init__(self, driver):
        self.driver = driver

class LoginPage(BasePage):
    def open_page(self):
        self.open_page = True

        
    def login(self, username, password):
        if username == "user" and password == "pass":
            self.login_in = True
        else:
            self.login_in = False
        

def test_login_success():
    driver = object()
    page = LoginPage(driver)

    page.open_page()
    page.login("user", "pass")

    assert page.login_in == True