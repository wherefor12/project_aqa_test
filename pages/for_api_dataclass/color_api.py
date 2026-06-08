from pydantic import BaseModel, field_validator
import os
from dotenv import load_dotenv
import requests

load_dotenv()

class Color(BaseModel):
    id: int
    name: str
    color: str
    year: int

class ColorsApi:
    BASE_URL = "https://reqres.in/api/unkown"
    
    def __init__(self):
        api_key = os.getenv("API_KEY")
        self.headers = {"x-api-key": api_key}

    def get_colors(self):
        response = requests.get(self.BASE_URL, headers=self.headers)
        response.raise_for_status()
        raw_items = response.json()["data"]

        colors = []
        for item in raw_items:
            color = Color(
                id=item["id"],
                name=item["name"],
                color=item["color"],
                year=item["year"]
            )    
            colors.append(color)
        return colors
        


