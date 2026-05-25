LOGIN_URL = "https://github.com/login"
HOME_URL = "https://github.com/"
ERROR_URL = "https://github.com/session"


class AuthPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(LOGIN_URL)

    def login(self, username, password):
        self.page.get_by_label("Username or email address").fill(username)
        self.page.get_by_label("Password").fill(password)
        self.page.get_by_role("button", name="Sign in").click()

    

    