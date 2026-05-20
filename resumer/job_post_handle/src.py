from playwright.sync_api import sync_playwright


class Robot:
    def __init__(self, url: str, headless: bool = False):
        self.url = url
        self.headless = headless
        self.ttl = 5000  # milliseconds

    def set_ttl(self, milliseconds: int):
        self.ttl = milliseconds

    def start(self):
        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            headless=self.headless
        )

        self.page = self.browser.new_page()
        self.page.set_default_timeout(self.ttl)
        self.page.goto(self.url)

    def locate(self, selector):
        return self.page.locator(selector)

    # def get_by_role(self, role, name):
    #     return self.page.get_by_role(role, name=name)
    #
    # def get_by_xpath(self, xpath):
    #     return self.page.locator(f"xpath={xpath}")
    #
    # def get_by_label(self, label):
    #     return self.page.get_by_label(label)
    #
    # def get_by_text(self, text):
    #     return self.page.get_by_text(text)
    #
    # def write(self, selector: str, text: str):
    #     element = self.page.locator(selector)
    #     element.fill(text)
    #
    #     return element
    #
    # def click(self, selector: str):
    #     element = self.page.locator(selector)
    #     element.click()
    #
    #     return element
    #
    # def press(self, selector: str, key: str):
    #     element = self.page.locator(selector)
    #     element.press(key)
    #
    #     return element

    def text(self, selector: str) -> str:
        return self.locate(selector).inner_text()

    def html(self, selector: str) -> str:
        return self.locate(selector).inner_html()

    def exists(self, selector: str) -> bool:
        return self.locate(selector).count() > 0

    def pause_robot(self):
        # input("Press ENTER to continue...")
        self.page.pause()

    def close(self):
        self.browser.close()
        self.playwright.stop()


class JobPostHandler:
    def __init__(self, url: str, *options) -> None:
        self.url = url
        self.robot = Robot(url)
        self.job_description = None

    def set_job_description(self, jd):
        """
        If preferred manually, this method
        can be used to memoize the job description,
        skipping the step where the robot tries
        find the job description itself
        """
        self.job_description = jd
