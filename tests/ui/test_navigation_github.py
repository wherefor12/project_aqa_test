import pytest
from pages.for_github_testing.home_page import HomePage
from pages.for_github_testing.solutions_menu import SolutionsMenu
from pages.for_github_testing.CiCd_page import CiCd
from pages.for_github_testing.ContactSales_page import ContactSalesPage

@pytest.mark.ui
def test_navigation_github(page):
    first_name = "Yasha"
    last_name = "Test"

    home_page = HomePage(page)
    solutions_menu = SolutionsMenu(page)
    cicd_page = CiCd(page)
    contact_sales_page = ContactSalesPage(page)

    home_page.open()
    home_page.go_to_solutions()
    solutions_menu.select_cicd()
    cicd_page.click_contact_sales()
    contact_sales_page.fill_form(first_name, last_name)

    assert contact_sales_page.get_field_value("First name") == first_name
    assert contact_sales_page.get_field_value("Last name") == last_name