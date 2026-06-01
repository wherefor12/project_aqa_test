class SearchPage:
    URL = "https://duckduckgo.com"
    
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(self.URL)

    def search(self, text):
        self.page.locator("#searchbox_input").fill(text)
        self.page.locator("//span[@class='search-input_searchText__T0V7_']").click()
        self.page.locator("[data-testid='result']").first.wait_for()

    def get_results(self):
        return self.page.locator("[data-testid='result']").count()
        
