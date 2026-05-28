class SolutionsMenu:
    def __init__(self, page):
        self.page = page

    def select_cicd(self):
        self.page.get_by_role("link", name="CI/CD").click()