import pytest
from pages.github_change_topics_on_platform.home_page import HomePage
from pages.github_change_topics_on_platform.platform_section import PlatformSection

EXPECTED_LINKS = ["Features", "Enterprise", "Copilot", "AI", "Security", "Pricing"]

def test_search_platform(page):
    home_page = HomePage(page)
    platform_section = PlatformSection(page)
    
    home_page.open()
    
    actual_links = platform_section.platform_links()

    for link in EXPECTED_LINKS:
        assert link in actual_links, f"ссылка '{link}' не найдена:"
    