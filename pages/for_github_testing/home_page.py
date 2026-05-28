HOME_URL = "https://github.com/"

class HomePage:
    def __init__(self,page):
        self.page = page

    def open(self):
        self.page.goto(HOME_URL)

    def go_to_solutions(self):
        self.page.get_by_role("button", name = "Solutions").click()