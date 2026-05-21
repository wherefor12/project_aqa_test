from pages.base_pages import BasePage

class LoginPage(BasePage):
    def open_page(self):
        self.open_page = True

    def login(self, username, password):
        if username == "user" and password == "pass":
            self.login_in = True
        else:
            self.login_in = False