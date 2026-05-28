class ContactSalesPage:
    def __init__(self, page):
        self.page = page

    def fill_form(self, first_name, last_name):
        self.page.get_by_label("First name").fill(first_name)
        self.page.get_by_label("Last name").fill(last_name)

    def get_field_value(self, field_name):
        return self.page.get_by_label(field_name).input_value()