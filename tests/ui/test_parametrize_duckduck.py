import pytest
from pages.parametrize_search.search_page import SearchPage

@pytest.mark.parametrize("text", ["qa", "aqa", "python"])
def test_parametrize_duckduck(page, text):
    search_page = SearchPage(page)

    search_page.open()
    search_page.search(text)

    results_count = search_page.get_results()
    assert results_count > 5, f"По запросу '{text}' найдено меньше 5 результатов:"
