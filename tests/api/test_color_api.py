import pytest
import requests
from pages.for_api_dataclass.color_api import ColorsApi, Color

def test_get_colors(colors):
    for color in colors:
        assert color.year >= 2000, f"color name: {color.name}, year: {color.year}"

def test_name(colors):
    for color in colors:
        assert color.name.strip(), f"id{color.id}: пустое name"
