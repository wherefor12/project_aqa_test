class PlatformSection:
    def __init__(self, page):
        self.page = page

    def platform_links(self):
        heading = self.page.get_by_role("heading", name = "Platform")
        container = heading.locator("xpath=..")
        links = container.locator("a")
        return links.all_text_contents()