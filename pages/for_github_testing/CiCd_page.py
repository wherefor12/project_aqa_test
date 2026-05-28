class CiCd:
    def __init__(self, page):
        self.page = page

    def click_contact_sales(self):
        self.page.locator("(//span[@class='Primer_Brand__Button-module__Button__text___Z3ocU'])[2]").click()